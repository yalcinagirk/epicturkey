from django.urls import path, include

from django.contrib.auth.views import LoginView ,LogoutView
from blogsections.account import views as v

urlpatterns = [
    path('/login', LoginView.as_view(),name='login'),
    path('/', LogoutView.as_view(),name='logout'),

]
