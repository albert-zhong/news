# users/urls.py
from django.urls import path

from .views import SignUpView, UserListView, UserDetailView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail/<str:username>/', UserDetailView.as_view(), name='user_detail'),
    path('', UserListView.as_view(), name='user_list'),
]