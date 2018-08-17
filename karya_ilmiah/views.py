from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from pesan import pesan
from karya_ilmiah.models import KaryaIlmiah
from karya_ilmiah.form_tkj import Form_Karil_TKJ
from master.models import Siswa, Pembimbing

# Create your views here.
def karil_tkj(request):
    karil = KaryaIlmiah.objects.filter(nama__kelas__contains='TKJ').order_by('-tanggal_acc')
    return render(request, 'karil-tkj.html', {'karil':karil})

def karil_rpl(request):
    karil = KaryaIlmiah.objects.filter(nama__kelas__contains='RPL').order_by('-tanggal_acc')
    return render(request, 'karil-rpl.html', {'karil':karil})

def add_karil(request):
    if request.POST:
        form = Form_Karil_TKJ(request.POST)
        if form.is_valid():
            siswa = Siswa.objects.get(id=request.POST['nama'])
            pembimbing = Pembimbing.objects.get(id=request.POST['pembimbing'])
            KaryaIlmiah(
                nama = siswa,
                judul = request.POST['judul'],
                tanggal_acc = request.POST['tanggal_acc'],
                pembimbing = pembimbing,
            ).save()

            # ubah status_judul disini
            Siswa.objects.filter(id=request.POST['nama']).update(status_judul=True)

            msg = pesan().add()
            form = Form_Karil_TKJ()

            tkj = Siswa.objects.filter(kelas__contains='XII.TKJ', status_judul=False).order_by('kelas')
            rpl = Siswa.objects.filter(kelas__contains='XII.RPL', status_judul=False).order_by('kelas')
            return render(request, 'add-karil.html', {
                'msg': msg,
                'form': form,
                'tkj': tkj,
                'rpl': rpl,
            })
    else:
        form = Form_Karil_TKJ()
        tkj = Siswa.objects.filter(kelas__contains='XII.TKJ', status_judul=False).order_by('kelas')
        rpl = Siswa.objects.filter(kelas__contains='XII.RPL', status_judul=False).order_by('kelas')
    return render(request, 'add-karil.html', {
        'form': form,
        'tkj': tkj,
        'rpl': rpl,
    })
