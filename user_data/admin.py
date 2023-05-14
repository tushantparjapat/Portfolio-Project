from django.contrib import admin

# Register your models here.
from .models import Education ,skill,Experience,Project

class skilldisplay(admin.ModelAdmin):
    search_fields=('s_name',)
    list_display=['user','s_name']
    list_filter=['user','s_name']

class Educationdisplay(admin.ModelAdmin):
    search_fields=('c_name',)
    list_display=['user','c_name']
    list_filter=['user','c_name']
    
class Experiencedisplay(admin.ModelAdmin):
    search_fields=('post_name',)
    list_display=['user','post_name']
    list_filter=['user','post_name']
class Projectdisplay(admin.ModelAdmin):
    search_fields=('project_name',)
    list_display=['user','project_name']
    list_filter=['user','project_name']

admin.site.register(Education,Educationdisplay)

admin.site.register(skill,skilldisplay)
admin.site.register(Experience,Experiencedisplay)
admin.site.register(Project,Projectdisplay)