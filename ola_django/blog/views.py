from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'title': 'BLOG -',
        'posts': posts,
    }

    return render(request=request,
                  template_name='blog/index.html',
                  context=context)


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'EXEMPLO -'
    }

    return render(
        request=request,
        template_name='blog/exemplo.html',
        context=context
    )
