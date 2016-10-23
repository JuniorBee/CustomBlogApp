from django.views import generic
from .models import Post, Tag, Author
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, DateTimeForm


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]


class TagsList(generic.ListView):
    template_name = 'blog/tags_filter.html'
    context_object_name = 'tags_list'

    def get_queryset(self):
        return Tag.objects.all()


def author_by_nick(request, nick):
    author = get_object_or_404(Author, nick=nick)
    context = dict()
    context['posts_list'] = author.post_set.all()
    context['author'] = author
    return render(request, 'blog/post_list.html', context)


def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag_name=tag_name)
    all_posts = Post.objects.all()
    posts_with_tag = [post for post in all_posts if tag in post.tags.all()]
    context = {'posts_list': posts_with_tag}
    print(tag_name, tag)
    return render(request, 'blog/post_list.html', context)


def publication_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def posts_by_date(request, year=0, month=0, day=0, week=0):
    posts_list = Post.objects.filter(pub_date__year=year)
    print(year, month, day, week)
    if week != 0:
        new_list = []
        for post in Post.objects.filter(pub_date__year=year):
            if post.pub_date.isocalendar()[1] == week:
                new_list.append(post)
        posts_list = new_list
    if month != 0:
        posts_list = Post.objects.filter(pub_date__year=year, pub_date__month=month)
    if day != 0:
        posts_list = Post.objects.filter(pub_date__year=year,
                                         pub_date__month=month, pub_date__day=day)
    context = {'posts_list': posts_list}
    print(context)
    return render(request, 'blog/post_list.html', context)


def add_post(request):
    form = PostForm
    return render(request, 'blog/add_post.html', {'form': form})


def filter_form(request):
    if request.method == 'POST':
        form = DateTimeForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            year = form['year']
            month = form['month']
            day = form['day']
            return redirect('posts_by_date', year, month, day)
