from django.contrib import admin

from master.models import Siswa, Instansi, InstansiTKJ

# Register your models here.
class SiswaAdmin(admin.ModelAdmin):
    list_display = ['NIS', 'nama', 'kelas', 'pkl']
    list_filter = ('kelas', 'program_ahli', 'pkl')
    search_fields = ['NIS', 'nama']
    list_per_page = 20

    actions = ['dapat_tempat_pkl', 'belum_dapat_tempat_pkl']

    def dapat_tempat_pkl(self,request,queryset):
        queryset.update(pkl=True)

    def belum_dapat_tempat_pkl(self,request,queryset):
        queryset.update(pkl=False)

class InstansiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat']
    search_fields = ['nama', 'alamat']
    list_per_page = 20

class InstansiTKJAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat']
    search_fields = ['nama', 'alamat']
    list_per_page = 20

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Instansi, InstansiAdmin)
admin.site.register(InstansiTKJ, InstansiTKJAdmin)
