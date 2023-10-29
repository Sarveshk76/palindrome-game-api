from django.urls import path
from .api_views import (GameCrudAPIView, GameListAPIView)

urlpatterns = [
    path('', GameCrudAPIView.as_view(), name='game_crud_api_view'),
    path('list/', GameListAPIView.as_view(), name='game_list_api_view')
]
