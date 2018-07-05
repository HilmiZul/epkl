from django.contrib import admin
from akun.models import Akun

# Register your models here.
class AkunAdmin(admin.ModelAdmin):
    list_display = ['username', 'nama_depan', 'nama_belakang']
    search_fields = ['username', 'nama_depan', 'nama_belakang']
    list_per_page = 20

admin.site.register(Akun, AkunAdmin)
