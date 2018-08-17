from django.contrib import admin
from karya_ilmiah.models import KaryaIlmiah

# Register your models here.
class KaryaIlmiahAdmin(admin.ModelAdmin):
    list_display = ['judul', 'nama']
    search_fields = ['judul', 'nama']
    list_per_page = 30

admin.site.register(KaryaIlmiah, KaryaIlmiahAdmin)
