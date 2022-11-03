from django.http import HttpResponse, JsonResponse

# HttpResponse se usa cuando voy a pintar el front con django o cuando envio HTML

def htmlbase(request):
    return HttpResponse("<h1>Hello, world</h1> You're at the articles index.")

def jsonbase(request):
    return JsonResponse({"name": "hello", "values":[1,2,3]})
