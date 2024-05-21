from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)   #This sets up the one to many relation as a single user can have many tasks and if the user gets deleted all the tasks will get deleted by using this foreign key setup
    title = models.CharField(max_length=250,null=True)
    desc = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) #it sets the timeStamp defaulty

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #this is like filetering the data using the completed stamp
