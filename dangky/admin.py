from django.contrib import admin

# Register your models here.
from dangky.models import NguoiDung

class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap','email')
    list_display_links = ('ten_dang_nhap','email')
    list_filter = ('ten_dang_nhap','email')
    search_fields = ('ten_dang_nhap','email')
    list_per_page = 20

admin.site.register(NguoiDung, NguoiDungAdmin)