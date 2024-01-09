from django.urls import path
from . views import SignUpView, UserLoingView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', SignUpView.as_view(), name = 'register'),
    path('login/', UserLoingView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = 'logout')
]
