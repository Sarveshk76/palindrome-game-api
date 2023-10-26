from django.urls import path
from .api_views import UserCrudAPIView

urlpatterns = [
    path('user/', UserCrudAPIView.as_view(), name='user_crud_api_view'),
]