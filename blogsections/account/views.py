from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name= 'registration/login.html'

class LogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
