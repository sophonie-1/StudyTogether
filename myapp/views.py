from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from django.db.models import Q
from .models import *
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import RomModelForm


class RegisterCreateView(CreateView):
    form_class=UserCreationForm
    template_name = "registration/login_registration.html"
    redirect_authenticated_user =True
    success_url=reverse_lazy('myapp:home-view')

    def form_valid(self, form):
        response=super().form_valid(form)
        username=form.cleaned_data.get('username')
        password =form.cleaned_data.get('password1')

        user=authenticate(self.request,username=username,password=password)
        print(user)

        if user is not None:
            login(self.request,user)
        return response
    

    
    
    
class LoginCustomView(LoginView):
    redirect_authenticated_user =True
    template_name = "registration/login_view.html"
    success_url=reverse_lazy('myapp:home-view')

class UserProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'myapp/user_profile.html'
    context_object_name = 'user_profile'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['rooms'] = user.rommodel_set.all()
        context['recent_comments'] = user.messagemodel_set.all()
        context['topics'] = TopicModel.objects.all()
        return context
    
class UserProfileViewV(LoginRequiredMixin,View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        user_rooms = user.rommodel_set.all()
        user_messages = user.messagemodel_set.all()
        context = {
            'user_profile': user,
            'user_rooms': user_rooms,
            'user_messages': user_messages
        }
        return render(request, 'myapp/user_profile.html', context)



class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        query=self.request.GET.get('query') or ''
        rooms=RomModel.objects.filter(
            Q(topic__topic_name__icontains=query) |
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(host__username__icontains=query)
            )
        topics=TopicModel.objects.order_by('-created','-updated')
        Recent_comments = MessageModel.objects.filter(
            Q(rom__topic__topic_name__icontains=query) |
            Q(rom__name__icontains=query) |
            Q(rom__description__icontains=query) |
            Q(rom__host__username__icontains=query)
            )
        context={
            'rooms':rooms,
            'topics':topics,
            'recent_comments':Recent_comments,
        }
        return render(request,'myapp/home.html',context)
    
    


class RomeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        rom = get_object_or_404(RomModel, id=pk)
        room_messages = rom.messagemodel_set.all()
        participants = rom.participants.all()
        context = {
            'rom': rom,
            'room_messages': room_messages,
            'participants': participants
        }
        return render(request, 'myapp/rom.html', context)

    def post(self, request, pk):
        rom = get_object_or_404(RomModel, id=pk)
        action = self.request.POST.get('action')

        if action == 'delete':
            message_id = self.request.POST.get('message_id')
            if message_id:
                try:
                    comment = MessageModel.objects.get(id=message_id, rom=rom)
                    if comment.user == self.request.user or rom.host == self.request.user:
                        comment.delete()
                    else:
                        context = {
                            'rom': rom,
                            'room_messages': rom.messagemodel_set.all(),
                            'participants': rom.participants.all(),
                            'error': "You are not authorized to delete this message."
                        }
                        return render(request, 'myapp/rom.html', context)
                except MessageModel.DoesNotExist:
                    context = {
                        'rom': rom,
                        'room_messages': rom.messagemodel_set.all(),
                        'participants': rom.participants.all(),
                        'error': "Message not found."
                    }
                    return render(request, 'myapp/rom.html', context)
        else:  # Assume message creation
            body = self.request.POST.get('body')
            if body:
                MessageModel.objects.create(
                    user=self.request.user,
                    rom=rom,
                    body=body
                )
                rom.participants.add(self.request.user)
            else:
                context = {
                    'rom': rom,
                    'room_messages': rom.messagemodel_set.all(),
                    'participants': rom.participants.all(),
                    'form_error': "Message body cannot be empty."
                }
                return render(request, 'myapp/rom.html', context)
        
        return redirect('myapp:rom-view', pk=rom.id)
    
    
class CreateRoomView(LoginRequiredMixin,CreateView):
    template_name='myapp/room_form.html'
    form_class=RomModelForm
    success_url=reverse_lazy('myapp:home-view')

    def form_valid(self, form):
        writen_topic = form.cleaned_data.get('write_topic')
        if writen_topic:
            topic, created = TopicModel.objects.get_or_create(topic_name=writen_topic)
            form.instance.topic = topic
        form.instance.host = self.request.user
        response = super().form_valid(form)
        return response
        

    
    


class RomModelUpdateView(LoginRequiredMixin,UpdateView):
    model = RomModel
    template_name = "myapp/room_form.html"
    fields=('topic','name','description')
    success_url=reverse_lazy('myapp:home-view')

class RomModelDeleteView(LoginRequiredMixin,DeleteView):
    model = RomModel
    template_name = "myapp/delete-room.html"
    success_url=reverse_lazy('myapp:home-view')
