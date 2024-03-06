from django.contrib import admin

# Register your models here.
from MovieApp.models import Hero,Heroin,Director,Theater,Movie,Customer
# Register your models here.
admin.site.register(Hero)
admin.site.register(Heroin)
admin.site.register(Director)
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Customer)
