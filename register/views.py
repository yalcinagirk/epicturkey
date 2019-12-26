# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/")
	else:
		form = RegisterForm()

	return render(response, "registration/register.html", {"form":form})
def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
