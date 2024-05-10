from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fields(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    fields = models.ForeignKey(Fields , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='default/default_employee.jpg')

    def __str__(self):
        return str(self.name)
    

class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='news/', default='default/default_news.jpg')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True , on_delete=models.PROTECT)
    def __str__(self):
        return str(self.title)
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)