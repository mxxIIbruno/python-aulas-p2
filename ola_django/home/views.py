from django.shortcuts import render


def home(request):
    print('home')
    return render(
        request=request, template_name='home/index.html'
    )
