from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForgeinKey(Group, blank = True, null = True, related_name="posts") #related_name здесь не нужен?

class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField() #такой должен быть тип поля?
    description = models.TextField()
    def __str__(self):
        return self.title 
