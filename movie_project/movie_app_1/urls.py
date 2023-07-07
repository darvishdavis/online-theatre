from django.urls import path
from movie_app_1 import views
app_name = 'movie-app-1'
urlpatterns = [
    path('', views.default, ),
    path('home/', views.home, ),
    path('movie/<int:film_id>/', views.movie, name='details'),
    path('add/', views.add, name='add'),
    path('edit/<int:film_id>/', views.edit, name='edit'),
    path('delete/<int:film_id>/', views.delete, name='delete')
]