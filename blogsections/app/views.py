from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from blogsections.app.models import Cities,Comments
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Create your views here.


class HomeView(TemplateView):
    template_name = "app/home.html"

class AboutView(TemplateView):
    template_name = "app/about.html"


class CityDetails(DetailView):
    template_name = 'app/city.html'

    def get_object(self):
        city_id = self.kwargs.get("id")
        return get_object_or_404(Cities, id=city_id)
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        city_id = self.kwargs.get('id')
        context['city_id'] = city_id
        return context
class CitiesView(ListView):
    model = Cities
    template_name = 'app/Cities.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(CitiesView, self).get_context_data(**kwargs)
        list_exam = Cities.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context









