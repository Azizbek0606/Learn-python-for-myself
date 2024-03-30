from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    
class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image   = models.ImageField(blank=True , upload_to="blog/")
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.comment)

class Like(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.author)

class View(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.author)