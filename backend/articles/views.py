import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Comment


def htmlbase(request):
    # HttpResponse se usa cuando voy a pintar el front con django o cuando envio HTML
    return HttpResponse("<h1>Hello, world</h1> You're at the articles index.")

def jsonbase(request):
    # JsonResponse se usa cuando voy a responder con json (para frameworks javascript)
    return JsonResponse({"name": "hello", "values":[1,2,3]})

def prueba(request):
    # all_items = Article.objects.all() # todos los objectos de este modelo
    # filtered_items = Article.objects.filter(title = 'Prueba') # filtro todos los objetos que cumplan x condición
    filtered_items = Article.objects.filter(title__contains = 'Titulo')
    items_json = []
    for item in filtered_items: 
        # serializamos los objetos creados a partir de un modelo
        items_json.append({'id':item.id, 'title':item.title, 'body':item.body})
    return JsonResponse({'results':items_json})


def get_all_articles(request):
    items = Article.objects.all()
    items_json = []
    for item in items: 
        items_json.append({'id': item.id, 'title': item.title, 'body': item.body})
    return JsonResponse({'results':items_json})

def get_article_by_id(request, pk):
    item = Article.objects.get(id=pk)
    return JsonResponse({'id':item.id, 'title':item.title, 'body':item.body})

@csrf_exempt
def create_article(request):
    data = json.loads(request.body)
    title_value = data['title']
    body_value = data['body']
    item = Article(title=title_value, body=body_value)
    item.save()
    return JsonResponse({'id':item.id, 'title':item.title, 'body':item.body})

@csrf_exempt
def delete_article(request, pk):
    item = Article.objects.get(id=pk)
    item.delete()
    return JsonResponse({'status':'OK'})



import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CommentSerializer(ModelSerializer):

    user = serializers.SerializerMethodField(method_name="get_user_real_username")
    random = serializers.SerializerMethodField()

    def get_user_real_username(self, comment):
        return comment.user.username

    def get_random(self, comment):
        return random.randint(0, 10)

    class Meta:
        model = Comment
        fields = ("body", "created_date", "user", "random")


class CommentViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, pk):
        if pk == '3':
            return Response({"metodo": "sobreescrito"})
        return super().retrieve(request, pk)
