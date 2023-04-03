#  Xudikk  2023/3/29
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.contrib import admin

# Register your models here.
from api.models.errors import Error


@admin.register(Error)
class ErrorAdminModel(admin.ModelAdmin):
    list_display = [field.name for field in Error._meta.fields]