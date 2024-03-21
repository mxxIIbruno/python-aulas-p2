from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Olá home',
        'title': 'HOME -'
    }

    return render(
        request=request,
        template_name='home/index.html',
        context=context
    )
