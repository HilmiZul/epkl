from django.contrib import admin

from letter.models import Permohonan

# Register your models here.
class PermohonanAdmin(admin.ModelAdmin):
    list_display = ['nama_siswa', 'nama_instansi']
    search_fields = ['nama_siswa']
    list_filter = ('nama_instansi',)
    list_per_page = 20

admin.site.register(Permohonan, PermohonanAdmin)
