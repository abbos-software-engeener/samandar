from django.urls import path
from .views import View, DetailView

app_name = 'main'


urlpatterns = [
    path('book/',DetailView.as_view()),
    path('book/<int:pk>/',View.as_view()),
]