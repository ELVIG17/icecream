from django.http import HttpResponse

def ice_cream_list(request):
    # Запрос к ice_cream/
    return HttpResponse('Каталог мороженого')

def ice_cream_detail(request, pk):
    # Запрос к ice_cream/<число>/
    # f-строка позволяет легко вставить переменную pk в текст
    return HttpResponse(f'Мороженое номер {pk}')
