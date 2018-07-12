from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from master.models import *
from letter.models import *

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    siswa_tkj = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan').count()
    siswa_rpl = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak').count()

    instansi_tkj = InstansiTKJ.objects.all().count()
    instansi_rpl = Instansi.objects.all().count()

    siswa_tkj_get_pkl = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan', pkl=True).count()
    siswa_rpl_get_pkl = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak', pkl=True).count()

    siswa_tkj_not_pkl = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan', pkl=False).count()
    siswa_rpl_not_pkl = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak', pkl=False).count()

    return render(request, 'dashboard.html',
        {
            'siswa_tkj':siswa_tkj,
            'siswa_rpl':siswa_rpl,
            'instansi_tkj':instansi_tkj,
            'instansi_rpl':instansi_rpl,
            'siswa_tkj_get_pkl':siswa_tkj_get_pkl,
            'siswa_rpl_get_pkl':siswa_rpl_get_pkl,
            'siswa_tkj_not_pkl':siswa_tkj_not_pkl,
            'siswa_rpl_not_pkl':siswa_rpl_not_pkl,
        }
    )
