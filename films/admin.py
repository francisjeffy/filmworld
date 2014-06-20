from django.contrib import admin
from films.models import Film
from films.models import Director

admin.site.register(Film)
admin.site.register(Director)