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

    # DELETE
    path('<int:id>/delete/', views.delete, name='delete'),

    # UPDATE
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
]
