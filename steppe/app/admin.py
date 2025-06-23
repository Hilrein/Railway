from django.contrib import admin

# Register your models here.

from .models import Trains, Route, Schedule, Wagon, WagonType, TicketPrice, Reviews, Cities, Tickets, Questions

admin.site.register(WagonType)
admin.site.register(Wagon)
admin.site.register(TicketPrice)
admin.site.register(Reviews)
admin.site.register(Cities)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('get_formatted_datetime', 'train')  # Указание полей для отображения в списке объектов

class TrainsAdmin(admin.ModelAdmin):
    list_display = ('number', 'route') 

class RoutesAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'route_stations') 

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Trains, TrainsAdmin)
admin.site.register(Route, RoutesAdmin)

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'train', 'wagon', 'seat', 'purchase_date', 'price') 

admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Questions)

# Импорт модуля admin из библиотеки Django.contrib
from django.contrib import admin
# Импорт модели MyModel из текущего каталога (".")
from .models import MyModel
# Регистрация модели MyModel для административного сайта
admin.site.register(MyModel)