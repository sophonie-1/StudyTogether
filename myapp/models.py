from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture= models.ImageField(upload_to='profile_images', default='image-1.jpg')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        ordering = ['user__username']



class TopicModel(models.Model):
    topic_name=models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_name
    class Meta:
        ordering=['-updated','-created']

class RomModel(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(TopicModel,on_delete=models.SET_NULL,null=True,related_name='topic-roms+')
    participants=models.ManyToManyField(User,related_name='participants')
    name=models.CharField(max_length=100)
    description =models.TextField()
    updated=models.DateTimeField(auto_now=True) 
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['-updated','-created']
class MessageModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rom=models.ForeignKey(RomModel,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:15]
    
    class Meta:
        ordering=['-updated','-created']
    