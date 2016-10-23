from django.db.models import Model
from django.db import models


class Tag(Model):
    tag_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.tag_name


class Author(Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nick = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nick


class Blog(Model):
    author = models.ForeignKey(Author)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='blog/pictures/')

    def __str__(self):
        return self.name


class Post(Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    image = models.ImageField(blank=True, upload_to='blog/pictures/')
    tags = models.ManyToManyField(Tag, blank=True)
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(Author, blank=True)

    def __str__(self):
        return self.header
