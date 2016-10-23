from django import template
from blog.forms import DateTimeForm

register = template.Library()


@register.assignment_tag
def datetimeform():
    return DateTimeForm
