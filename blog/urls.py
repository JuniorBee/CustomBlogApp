from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .models import Post

app_name = 'blog'

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Post.objects.all().order_by('-pub_date')[:20],
                         template_name='post_list.html',
                         context_object_name='posts_list'),
        name='post_list'),

    url(r'@(?P<nick>[a-zA-Z0-9_]+)/$', views.author_by_nick, name='author_by_nick'),
    url(r'tags/(?P<tag_name>[a-zA-Z0-9_]+)/$', views.posts_by_tag, name='posts_by_tag'),
    url(r'post(?P<post_id>[0-9]+)/$', views.publication_detail, name='publication_detail'),
    url(r'by_date/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<week>[0-9]+)/$',
        views.posts_by_date, name='posts_by_date'),
    url(r'add_post', views.add_post, name='add_post'),
    url(r'filter_form', views.filter_form, name='filter_form')
]
