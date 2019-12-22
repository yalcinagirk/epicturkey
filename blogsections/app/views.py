from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from blogsections.app.models import Cities, Article, City
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Create your views here.


class HomeView(TemplateView):
    template_name = "app/home.html"

class AboutView(TemplateView):
    template_name = "app/about.html"

class CitiesView(ListView):
    model = Cities
    city = Cities.objects.get(id=1)
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
class CityView(ListView):
    model = City
    template_name = 'app/city.html'
    paginate_by = 4








