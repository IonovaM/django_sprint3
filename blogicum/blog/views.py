from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index_posts(posts):
    current_time = timezone.now()

    posts = posts.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).select_related('category').order_by('pub_date').reverse()

    return posts


def index(request):
    posts = index_posts(Post.objects)
    template='blog/index.html'
    context={
        'post_list': posts[0:5]
    }
    return render(request, template, context)


def post_detail(request, post_id):
    current_time = timezone.now()
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    posts = index_posts(Post.objects)
    template = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = index_posts(category.posts)
    context = {
        'post_list': posts,
        'category': category
    }
    return render(request, template, context)
