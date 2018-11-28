from django.contrib import admin
from main.models import Person, Achievements, Category

# Register your models here.
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Achievements)

