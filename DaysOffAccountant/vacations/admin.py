from .models import Vacation
from django.contrib import admin
from .models import Vacation


class VacationAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'user')
    list_filter = ('user',)


admin.site.register(Vacation, VacationAdmin)
