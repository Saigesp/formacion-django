"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
