from django.shortcuts import render


def blog(request):
    print('blog')
    return render(
        request=request, template_name='blog/index.html'
    )


def exemplo(request):
    print('exemplo')
    return render(
        request=request, template_name='blog/exemplo.html'
    )
