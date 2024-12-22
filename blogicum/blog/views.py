from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index_posts(posts):
    dt_now = timezone.now()
    posts = posts.filter(
        pub_date__lte=dt_now,
        is_published=True,
        category__is_published=True
    )
    return posts.order_by('-pub_date')


def index(request):
    posts = index_posts(Post.objects)
    # posts.order_by('pub_date')
    return render(request, 'blog/index.html', {'post_list': posts[0:5]})


def post_detail(request, post_id):
    dt_now = timezone.now()
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lte=dt_now,
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = index_posts(category.posts)
    return render(
        request,
        'blog/category.html',
        {
            'post_list': posts,
            'category': category
        }
    )
