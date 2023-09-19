from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'main/home.html', {'title': 'Основная страница'})

def aboutPage(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})
