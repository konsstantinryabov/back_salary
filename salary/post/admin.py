from django.contrib import admin
from post.models import Salary


class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'salar',
                    'date')


admin.site.register(Salary, SalaryAdmin)
