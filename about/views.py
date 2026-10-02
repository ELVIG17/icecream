from django.shortcuts import render

def description(request):
    # Шаблон templates/about/description.html
    return render(request, 'about/description.html')
