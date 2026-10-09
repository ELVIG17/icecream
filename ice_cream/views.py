from django.shortcuts import render

# Добавляем список каталога в начало файла
ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, '
                       'для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир'
                       ' — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]

def ice_cream_list(request):
    """Отображает список всех видов мороженого"""
    template = 'ice_cream/list.html'
    context = {'ice_creams': ice_cream_catalog}
    return render(request, template, context)


def ice_cream_detail(request, pk):
    """
    Отображает детальную страницу мороженого по ID (pk).
    По условию: если ID не существует — пусть будет ошибка list index out of range.
    """
    template = 'ice_cream/detail.html'
    # Берем элемент из списка по индексу pk
    ice_cream = ice_cream_catalog[pk]
    
    context = {
        'ice_cream': ice_cream
    }
    return render(request, template, context)
