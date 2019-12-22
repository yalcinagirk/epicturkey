from django.contrib import admin

# Register your models here.
from blogsections.app.models import Cities,Articles,Article

admin.site.register(Cities)
admin.site.register(Articles)
admin.site.register(Article)
