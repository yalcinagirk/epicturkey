from django.db import models

# Create your models here.
from django.urls import reverse


class Cities(models.Model):
    title = models.CharField(max_length=40, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='img/')
    user = models.ForeignKey('auth.User',
                             on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Articles(models.Model):
    city_name = models.ForeignKey(Cities,on_delete=models.CASCADE)
    title = models.CharField(max_length=40, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='img/')
    def __str__(self):
        return self.title

class Article(models.Model):
    article_name = models.ForeignKey(Articles, on_delete=models.CASCADE)
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.headline

