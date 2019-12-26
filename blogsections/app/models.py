from django.db import models

# Create your models here.
from django.urls import reverse


class Cities(models.Model):
    title = models.CharField(max_length=40, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='img/')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('city', kwargs={"id": self.id})
class Comments(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='img/')
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('city', kwargs={"id": self.id})







