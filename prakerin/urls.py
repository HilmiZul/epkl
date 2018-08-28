"""prakerin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from master import views as master_view
from letter import views as letter_view
from letter import views_report as letter_view_report
from tag import views as tag_view
from dashboard import views as dashboard_view
from akun import views_akun
from karya_ilmiah import views as karil_view
from karya_ilmiah import views_report as karil_view_report

urlpatterns = [
    url(r'^dapur/', admin.site.urls),

    url(r'^login/$', views_akun.akun_login),
    url(r'^logout/$', views_akun.akun_logout),
    url(r'^$', dashboard_view.dashboard),

    url(r'^master-tkj/$', master_view.master_tkj),
    url(r'^master-tkj/tambah/$', master_view.add_master_tkj),
    url(r'^master-tkj-1/$', master_view.master_tkj_1),
    url(r'^master-tkj-2/$', master_view.master_tkj_2),
    url(r'^master-tkj-3/$', master_view.master_tkj_3),
    url(r'^master-tkj-4/$', master_view.master_tkj_4),

    url(r'^surat-tkj/$', letter_view.surat_tkj),
    url(r'^surat-tkj/tambah/$', letter_view.tambah_surat_tkj),
    url(r'^surat-tkj/hapus/(\d+)', letter_view.hapus_surat_tkj),
    url(r'^surat-tkj/ubah/(\d+)', letter_view.ubah_surat_tkj),
    url(r'^surat-tkj/cetak-surat/(\d+)', letter_view_report.form_cetak_tkj),

    url(r'^master-tkj-1/ubah/(\d+)', master_view.ubah_tkj_1),
    url(r'^master-tkj-2/ubah/(\d+)', master_view.ubah_tkj_2),
    url(r'^master-tkj-3/ubah/(\d+)', master_view.ubah_tkj_3),
    url(r'^master-tkj-4/ubah/(\d+)', master_view.ubah_tkj_4),

    url(r'^master-tkj-1/hapus/(\d+)', master_view.delete_tkj_1),
    url(r'^master-tkj-2/hapus/(\d+)', master_view.delete_tkj_2),
    url(r'^master-tkj-3/hapus/(\d+)', master_view.delete_tkj_3),
    url(r'^master-tkj-4/hapus/(\d+)', master_view.delete_tkj_4),

    url(r'^master-rpl/$', master_view.master_rpl),
    url(r'^master-rpl/tambah/$', master_view.add_master_rpl),
    url(r'^master-rpl-1/$', master_view.master_rpl_1),
    url(r'^master-rpl-2/$', master_view.master_rpl_2),
    url(r'^master-rpl-3/$', master_view.master_rpl_3),

    url(r'^surat-rpl/$', letter_view.surat_rpl),
    url(r'^surat-rpl/tambah/$', letter_view.tambah_surat_rpl),
    url(r'^surat-rpl/hapus/(\d+)', letter_view.hapus_surat_rpl),
    url(r'^surat-rpl/ubah/(\d+)', letter_view.ubah_surat_rpl),

    url(r'^master-rpl-1/ubah/(\d+)', master_view.ubah_rpl_1),
    url(r'^master-rpl-2/ubah/(\d+)', master_view.ubah_rpl_2),
    url(r'^master-rpl-3/ubah/(\d+)', master_view.ubah_rpl_3),

    url(r'^master-rpl-1/hapus/(\d+)', master_view.delete_rpl_1),
    url(r'^master-rpl-2/hapus/(\d+)', master_view.delete_rpl_2),
    url(r'^master-rpl-3/hapus/(\d+)', master_view.delete_rpl_3),

    url(r'^master-instansi/rpl/$', master_view.master_instansi_rpl),
    url(r'^master-instansi/rpl/tambah/$', master_view.add_instansi_rpl),
    url(r'^master-instansi/rpl/hapus/(\d+)$', master_view.delete_instansi_rpl),
    url(r'^master-instansi/rpl/ubah/(\d+)$', master_view.ubah_instansi_rpl),

    url(r'^master-instansi/tkj/$', master_view.master_instansi_tkj),
    url(r'^master-instansi/tkj/tambah/$', master_view.add_instansi_tkj),
    url(r'^master-instansi/tkj/hapus/(\d+)$', master_view.delete_instansi_tkj),
    url(r'^master-instansi/tkj/ubah/(\d+)$', master_view.ubah_instansi_tkj),


    url(r'^cetak/(\d+)', letter_view_report.form_cetak),
    url(r'^laporan/', letter_view_report.laporan_permohonan),

    # NAME TAG
    url(r'^name-tag/$', tag_view.name_tag),
    url(r'^name-tag/tkj/$', tag_view.tag_tkj),
    url(r'^name-tag/rpl/$', tag_view.tag_rpl),
    url(r'^name-tag/tbsm/$', tag_view.tag_tbsm),

    url(r'^name-tag/tkj-1/$', tag_view.tag_tkj_1),
    url(r'^name-tag/tkj-2/$', tag_view.tag_tkj_2),
    url(r'^name-tag/tkj-3/$', tag_view.tag_tkj_3),
    url(r'^name-tag/tkj-4/$', tag_view.tag_tkj_4),

    url(r'^name-tag/rpl-1/$', tag_view.tag_rpl_1),
    url(r'^name-tag/rpl-2/$', tag_view.tag_rpl_2),
    url(r'^name-tag/rpl-3/$', tag_view.tag_rpl_3),

    url(r'^name-tag/tbsm/$', tag_view.tag_tbsm),
    url(r'^name-tag/tbsm-1/$', tag_view.tag_tbsm_1),
    url(r'^name-tag/tbsm-2/$', tag_view.tag_tbsm_2),
    url(r'^name-tag/tbsm-3/$', tag_view.tag_tbsm_3),
    url(r'^name-tag/tbsm-4/$', tag_view.tag_tbsm_4),

    url(r'^absensi/$', master_view.absensi),
    url(r'^absensi/cetak/$', master_view.cetak_absensi),

    url(r'^surat-rpl/cetak/$', letter_view_report.cetak_surat_rpl),
    url(r'^master-rpl/belum-pkl/$', letter_view_report.cetak_rpl_belum_pkl),

    url(r'^surat-tkj/cetak/$', letter_view_report.cetak_surat_tkj),
    url(r'^master-tkj/belum-pkl/$', letter_view_report.cetak_tkj_belum_pkl),

    url(r'^master-instansi/tkj/cetak/$', master_view.cetak_instansi_tkj),
    url(r'^master-instansi/rpl/cetak/$', master_view.cetak_instansi_rpl),

    url(r'^pembimbing/$', master_view.pembimbing),
    url(r'^pembimbing/tambah/$', master_view.add_pembimbing),
    url(r'^pembimbing/ubah/(\d+)', master_view.ubah_pembimbing),

    url(r'^karya-ilmiah/tkj/$', karil_view.karil_tkj),
    url(r'^karya-ilmiah/rpl/$', karil_view.karil_rpl),
    url(r'^karya-ilmiah/tambah/$', karil_view.add_karil),
    url(r'^karya-ilmiah/rpl/sunting/(\d+)$', karil_view.sunting_karil_rpl),
    url(r'^karya-ilmiah/tkj/sunting/(\d+)$', karil_view.sunting_karil_tkj),
    url(r'^karya-ilmiah/tkj/report/$', karil_view_report.report_karil_tkj),
    url(r'^karya-ilmiah/rpl/report/$', karil_view_report.report_karil_rpl),
    url(r'^karya-ilmiah/tkj/export/$', karil_view_report.export_karil_tkj, name='export_karil_tkj'),
    url(r'^karya-ilmiah/rpl/export/$', karil_view_report.export_karil_rpl, name='export_karil_rpl'),

    url(r'^surat-rpl/export/$', letter_view_report.export_pkl_rpl, name='export_pkl_rpl'),
    url(r'^surat-tkj/export/$', letter_view_report.export_pkl_tkj, name='export_pkl_tkj'),
]
