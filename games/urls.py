from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.game_form, name='game_form'),
]