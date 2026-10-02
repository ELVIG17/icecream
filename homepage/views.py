from django.shortcuts import render

def index(request):
    # Django сам найдёт templates/homepage/index.html
    return render(request, 'homepage/index.html')
