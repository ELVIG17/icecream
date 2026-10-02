from django.shortcuts import render

def ice_cream_list(request):
    # Шаблон templates/ice_cream/list.html
    return render(request, 'ice_cream/list.html')

def ice_cream_detail(request, pk):
    # Шаблон templates/ice_cream/detail.html
    # Пока передаём pk в шаблон, даже если в HTML он не используется
    context = {'pk': pk}
    return render(request, 'ice_cream/detail.html', context)
