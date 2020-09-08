from django.contrib import admin
from .models import Cinema, SeatClass, Screen, Show


admin.site.register(Cinema)
admin.site.register(Screen)
admin.site.register(SeatClass)
admin.site.register(Show)