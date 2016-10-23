from django.contrib import admin

from .models import Tag, Author, Blog, Post

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Post)