from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls), #viene por defecto
    path('html_base/', views.htmlbase, name='html_base'), # La property name es de uso interno de django ( testing etc )
    path('json_base/', views.jsonbase, name='json_base'),
    path('prueba/', views.prueba, name="get_articles"),
    path('articles/', views.get_all_articles, name="get_all_articles"),
    path('articles/<int:pk>/', views.get_article_by_id, name="get_article_by_id"),
    path('articles/create_article/', views.create_article, name="create_article"),
    path('articles/delete_article/<int:pk>/', views.delete_article, name="delete_article")
]


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'comentarios', views.CommentViewSet, basename="hola")
urlpatterns += router.urls
