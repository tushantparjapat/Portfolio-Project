
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from user_account.models import Profile
from datetime import date
from  uuid import uuid4
import os




class skill(models.Model):
    id = models.CharField(primary_key=True,max_length=50, default=uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skill" )
    s_name = models.CharField(max_length=100)
    

    def __str__(self) :
        return self.s_name

class Education(models.Model):
    id = models.CharField(primary_key=True,max_length=50, default=uuid4,editable=False)

    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="edu" )
    c_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

    description = models.CharField(max_length=100, default="")
    Grade = models.CharField(max_length=100,default="0")


    def __str__(self) :
        return self.c_name

class Experience(models.Model):
    id = models.CharField(primary_key=True,max_length=50, default=uuid4,editable=False)

    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="Experience" )
    post_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    
    description = models.CharField(max_length=100 ,default="")
    

    def __str__(self) :
        return self.post_name

class Project(models.Model):
    id = models.CharField(primary_key=True,max_length=50, default=uuid4,editable=False)

    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="Project" )
    project_name = models.CharField(max_length=100 )
    company_name = models.CharField(max_length=100, null=True)
    
    description = models.CharField(max_length=100 ,default="")

    def photo_path(self,filename):
        basefilename,file_extension = os.path.splitext(filename)
        # chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        
        return 'project_image/{userid}{ext}'.format(userid=self.user,ext=file_extension)

    image = models.ImageField(upload_to=photo_path, null=True ,default='G:\Workshop\django porjects\portfolio2\portfolio\static\assets\imgs\man.png')
    print('{userid}{name}'.format(userid=user,name=project_name))

    def __str__(self) :
        return self.project_name


