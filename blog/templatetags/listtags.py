from django import template
from blog.models import Author, Tag

register = template.Library()


@register.assignment_tag
def get_authors():
    return Author.objects.all()


@register.assignment_tag
def get_tags():
    return Tag.objects.all()
