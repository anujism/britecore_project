# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import RiskType, RiskField

class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


class RiskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CustomModelAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    search_fields = ['=id']

# Register your models here.
admin.site.register(RiskType, RiskTypeAdmin)
admin.site.register(RiskField, CustomModelAdmin)


