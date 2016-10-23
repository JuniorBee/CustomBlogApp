from django import template
from django.utils import timezone

register = template.Library()


@register.assignment_tag
def this_year():
    return timezone.now().year


@register.assignment_tag
def this_month():
    return timezone.now().month


@register.assignment_tag
def this_day():
    return timezone.now().day


@register.assignment_tag
def this_week():
    return timezone.now().isocalendar()[1]
