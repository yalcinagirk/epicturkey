from django.urls import include, path


urlpatterns = [
    path('',include('blogsections.app.urls'),name="app"),
    path('',include('blogsections.account.urls'),name="login"),
]
