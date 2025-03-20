from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # READ
    path('',views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # CREATE
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
