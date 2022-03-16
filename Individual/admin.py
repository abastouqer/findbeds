from django.contrib import admin
from Individual.models import User,EthenicityModel,StatsModel,CountryModel

admin.site.register(User)
admin.site.register(EthenicityModel)
admin.site.register(StatsModel)
admin.site.register(CountryModel)