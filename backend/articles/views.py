from django.http import HttpResponse, JsonResponse

from .models import Article

# HttpResponse se usa cuando voy a pintar el front con django o cuando envio HTML

def htmlbase(request):
    return HttpResponse("<h1>Hello, world</h1> You're at the articles index.")

def jsonbase(request):
    return JsonResponse({"name": "hello", "values":[1,2,3]})

def articles(request):
    items = Article.objects.all() #traigo todos los objectos creados a partir de este modelo
    filtered_items__insensitive_case = Article.objects.filter(title__contains = 'Titulo')
    filtered_items = Article.objects.filter(title = 'Prueba') #filtro todos los objetos que cumplan x condición
    items_json = []
    for item in filtered_items__insensitive_case: 
        items_json.append({'id':item.id, 'title':item.title, 'body':item.body}) #append es como push en js
    #linea 18 y 19 estamos serializando los objetos creados a partir de un modelo
    return JsonResponse({'results':items_json})
