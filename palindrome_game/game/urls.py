from django.urls import path
from .api_views import GameCrudAPIView

urlpatterns = [
    path('', GameCrudAPIView.as_view(), name='game_crud_api_view'),
]
