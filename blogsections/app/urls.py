from django.urls import include, path

from blogsections.app.views import HomeView, AboutView, CitiesView, DetailView, CityDetails

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('about/',AboutView.as_view(),name="about"),
    path('cities/',CitiesView.as_view(),name="cities"),
    path('city/<int:id>',CityDetails.as_view(),name="city"),

]


