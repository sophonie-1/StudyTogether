from django.contrib import admin
from .models import *
# Register your models here.
class RomAdmin(admin.ModelAdmin):
    list_display=['name','description','updated','created']
    search_fields=['name','description','host__username']
    list_filter=['host','topic','created','updated']


class MessageAdmin(admin.ModelAdmin):
    list_display=['user','rom','body','updated','created']
    search_fields=['user__username','rom__name','body']
    list_filter=['user','rom']

class TopicAdmin(admin.ModelAdmin):
    list_display=['topic_name','created','updated']
    search_fields=['topic_name']
    list_filter=['created','updated']

admin.site.register(RomModel,RomAdmin)
admin.site.register([MessageModel], MessageAdmin)
admin.site.register(TopicModel, TopicAdmin)
admin.site.register(UserProfile)