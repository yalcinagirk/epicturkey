from django.conf.urls import url
from django.urls import path, include

from django.contrib.auth.views import LoginView ,LogoutView

from blogsections import views
from blogsections.account.views import singIn, postsign, signUp, postsignup, logout

urlpatterns = [
    path('login/',singIn,name='login'),
    path('/', LogoutView.as_view(),name='logout'),
    path('postsign/', postsign),
    path('signup/',signUp,name='signup'),
    path('postsignup/',postsignup,name='postsignup'),
    path('logout/',logout,name="log"),

]
