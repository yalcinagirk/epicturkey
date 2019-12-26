from django.contrib import admin

# Register your models here.
from blogsections.app.models import Cities,Comments

admin.site.register(Cities)
admin.site.register(Comments)
