from django.shortcuts import render, redirect

from master.models import Siswa

# Create your views here.
def name_tag(request):
    return render(request, 'name-tag.html')


def tag_tkj(request):
    siswa = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan', pkl=True)
    return render(request, 'tag-tkj.html', {'siswa':siswa})

def tag_rpl(request):
    siswa = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak', pkl=True)
    return render(request, 'tag-rpl.html', {'siswa':siswa})

def tag_tbsm(request):
    siswa = Siswa.objects.filter(program_ahli='Teknik Sepeda Motor', pkl=False)
    return render(request, 'tag-tbsm.html', {'siswa':siswa})

def tag_tkj_1(request):
    siswa = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=True)
    return render(request, 'tag-tkj-1.html', {'siswa':siswa})

def tag_tkj_2(request):
    siswa = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=True)
    return render(request, 'tag-tkj-2.html', {'siswa':siswa})

def tag_tkj_3(request):
    siswa = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=True)
    return render(request, 'tag-tkj-3.html', {'siswa':siswa})

def tag_tkj_4(request):
    siswa = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=True)
    return render(request, 'tag-tkj-4.html', {'siswa':siswa})

def tag_rpl_1(request):
    siswa = Siswa.objects.filter(kelas='XII.RPL-1', pkl=True)
    return render(request, 'tag-rpl-1.html', {'siswa':siswa})

def tag_rpl_2(request):
    siswa = Siswa.objects.filter(kelas='XII.RPL-2', pkl=True)
    return render(request, 'tag-rpl-2.html', {'siswa':siswa})

def tag_rpl_3(request):
    siswa = Siswa.objects.filter(kelas='XII.RPL-3', pkl=True)
    return render(request, 'tag-rpl-3.html', {'siswa':siswa})

def tag_tbsm(request):
    siswa = Siswa.objects.filter(program_ahli='Teknik Sepeda Motor')
    return render(request, 'tag-tbsm.html', {'siswa':siswa})

def tag_tbsm_1(request):
    siswa = Siswa.objects.filter(kelas='XII.TBSM-1', pkl=False)
    return render(request, 'tag-tbsm.html', {'siswa':siswa})


def tag_tbsm_2(request):
    siswa = Siswa.objects.filter(kelas='XII.TBSM-2', pkl=False)
    return render(request, 'tag-tbsm.html', {'siswa':siswa})

def tag_tbsm_3(request):
    siswa = Siswa.objects.filter(kelas='XII.TBSM-3', pkl=False)
    return render(request, 'tag-tbsm.html', {'siswa':siswa})

def tag_tbsm_4(request):
    siswa = Siswa.objects.filter(kelas='XII.TBSM-4', pkl=False)
    return render(request, 'tag-tbsm.html', {'siswa':siswa})
