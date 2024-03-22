from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts


def blog(request):
    print("blog")

    context = {
        # 'text': 'Olá blog',
        "title": "BLOG -",
        "posts": posts,
    }

    return render(
        request=request,
        template_name="blog/index.html",
        context=context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        # 'text': 'Olá blog',
        "title": found_post['title'] + ' - ',
        "post": found_post,
    }

    return render(
        request=request,
        template_name="blog/post.html",
        context=context
    )


def exemplo(request):
    print("exemplo")

    context = {
        # 'text': 'Olá exemplo',
        "title": "EXEMPLO -"
    }

    return render(
        request=request,
        template_name="blog/exemplo.html",
        context=context
    )
