from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posted = models.DateTimeField(default=datetime.now(), 
                                db_index=True)
    coment = models.TextField()

    def __str__(self) -> str:
        return self.user.username + ': ' + str(self.id)

admin.site.register(Coment)

class Blog(models.Model):
    title = models.CharField(max_length=100,
                             unique_for_date="posted",)
    coments = models.ManyToManyField(Coment, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='img/', blank=True)
    description = models.TextField()
    content = models.TextField()
    posted = models.DateTimeField(default=datetime.now(), 
                                  db_index=True)
    
    def get_absolute_url(self):
        return reverse('blogpost', args=[str(self.id)])
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table= "Posts"

        ordering = ["-posted"]

admin.site.register(Blog)

