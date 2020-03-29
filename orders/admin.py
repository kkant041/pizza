from django.contrib import admin

from .models import regularpizza, sicilianpizza, topping, sub, pasta, salad, dinner_platter

# Register your models here.
admin.site.register(regularpizza)
admin.site.register(sicilianpizza)
admin.site.register(topping)
admin.site.register(sub)
admin.site.register(pasta)
admin.site.register(salad)
admin.site.register(dinner_platter)