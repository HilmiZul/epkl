from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from master.models import Instansi, Siswa
from letter.models import Permohonan

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def form_letter(request):
    instansi = Instansi.objects.order_by('nama')
    return render(request, 'form_letter.html', {'instansi':instansi})

# CETAK
@login_required(login_url=settings.LOGIN_URL)
def form_cetak(request,id_ins):
    '''if request.POST:
        get_req = request.POST['id_ins']
        if get_req is not None:
            meta_surat = Permohonan.objects.filter(nama_instansi_id=request.POST['id_ins'])
            instansi = Instansi.objects.get(id=request.POST['id_ins'])
            result = render(request, 'cetak.html', {'meta_surat':meta_surat, 'instansi':instansi})
        else:
            result = redirect('/')
    else:
        result = redirect('/')'''
    if id_ins is not None:
        meta_surat = Permohonan.objects.filter(nama_instansi_id=id_ins)
        instansi = Instansi.objects.get(id=id_ins)
        result = render(request, 'cetak.html', {'meta_surat':meta_surat, 'instansi':instansi})
    else:
        result = redirect('/')
    return result


# LAPORAN PERMOHONAN PKL
@login_required(login_url=settings.LOGIN_URL)
def laporan_permohonan(request):
    permohonan = Permohonan.objects.all().order_by('nama_instansi')
    return render(request, 'laporan.html', {'permohonans':permohonan})


##
# SURAT PERMOHONAN
@login_required(login_url=settings.LOGIN_URL)
def surat_rpl(request):
    surat = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
    return render(request, 'surat-rpl.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def ubah_surat_rpl(request,id_surat):
    if request.POST:
        s = Siswa.objects.get(id=request.POST['nama_siswa'])
        i = Instansi.objects.get(id=request.POST['nama_instansi'])

        Permohonan.objects.filter(id=id_surat).update(
            nama_siswa = s,
            nama_instansi = i,
        )
        msg = "Berhasil diperbaharui."
        surat = Permohonan.objects.get(id=id_surat)
        return render(request, 'ubah-surat-rpl.html', {'msg':msg, 'surat':surat})
    else:
        surat = Permohonan.objects.get(id=id_surat)
        siswa1 = Siswa.objects.filter(kelas='XII.RPL-1')
        siswa2 = Siswa.objects.filter(kelas='XII.RPL-2')
        siswa3 = Siswa.objects.filter(kelas='XII.RPL-3')
        instansis = Instansi.objects.all()
    return render(request, 'ubah-surat-rpl.html',
        {
            'surat':surat,
            'siswa1':siswa1,
            'siswa2':siswa2,
            'siswa3':siswa3,
            'instansis':instansis,
        }
    )



@login_required(login_url=settings.LOGIN_URL)
def surat_rpl_1(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.RPL-1').order_by('nama_instansi')
    return render(request, 'surat-rpl-1.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_rpl_2(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.RPL-2').order_by('nama_instansi')
    return render(request, 'surat-rpl-2.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_rpl_3(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.RPL-3').order_by('nama_instansi')
    return render(request, 'surat-rpl-3.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_tkj(request):
    surat = Permohonan.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi')
    return render(request, 'surat-tkj.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_tkj_1(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.TKJ-1').order_by('nama_instansi')
    return render(request, 'surat-tkj-1.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_tkj_2(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.TKJ-2').order_by('nama_instansi')
    return render(request, 'surat-tkj-2.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_tkj_3(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.TKJ-3').order_by('nama_instansi')
    return render(request, 'surat-tkj-3.html', {'surats':surat})

@login_required(login_url=settings.LOGIN_URL)
def surat_tkj_4(request):
    surat = Permohonan.objects.filter(nama_siswa__kelas='XII.TKJ-4').order_by('nama_instansi')
    return render(request, 'surat-tkj-4.html', {'surats':surat})

# HAPUS.TKJ
@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_tkj(request, id_surat):
    if request.POST:
        Permohonan.objects.filter(id=id_surat).delete()
        get_id_siswa = Permohonan.objects.filter(id=id_surat)
        Siswa.objects.filter(id=get_id_siswa__nama_siswa).update(pkl = False)
        msg = "Berhasil dihapus."
        get_surat = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
    else:
        return redirect('/surat-tkj/')
    return render(request, 'surat-tkj.html', {'msg':msg, 'surat':get_surat})


# HAPUS.RPL
@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_rpl(request, id_surat):
    if request.POST:
        Permohonan.objects.filter(id=id_surat).delete()
        get_id_siswa = Permohonan.objects.filter(id=id_surat)
        Siswa.objects.filter(id=get_id_siswa__nama_siswa).update(pkl = False)
        msg = "Berhasil dihapus."
        get_surat = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
    else:
        return redirect('/surat-rpl/')
    return render(request, 'surat-rpl.html', {'msg':msg, 'surat':get_surat})


##
# TAMBAH.SURAT.PERMOHONAN
@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_tkj(request):
    if request.POST:
        siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
        instansi = Instansi.objects.get(id=request.POST['nama_instansi'])
        Permohonan(
            perihal = "PKL",
            nama_siswa = siswa,
            nama_instansi = instansi
        ).save()
        Siswa.objects.filter(id=request.POST['nama_siswa']).update(pkl = True)
        msg = "Surat Permohonan berhasil ditambahkan."
        return render(request, 'tambah-surat-tkj.html', {'msg':msg})
    else:
        siswa1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False)
        siswa2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False)
        siswa3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False)
        siswa4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False)
        instansis = Instansi.objects.all()
        return render(request, 'tambah-surat-tkj.html',
            {'siswa1':siswa1, 'siswa2':siswa2, 'siswa3':siswa3, 'siswa4':siswa4, 'instansis':instansis}
        )

    return render(request, 'tambah-surat-tkj.html',
        {'siswa1':siswa1, 'siswa2':siswa2, 'siswa3':siswa3, 'siswa4':siswa4, 'instansis':instansis}
    )

@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_rpl(request):
    if request.POST:
        siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
        instansi = Instansi.objects.get(id=request.POST['nama_instansi'])
        Permohonan(
            perihal = "PKL",
            nama_siswa = siswa,
            nama_instansi = instansi
        ).save()
        # ubah status siswa menjadi True
        Siswa.objects.filter(id=request.POST['nama_siswa']).update(pkl = True)
        msg = "Surat Permohonan berhasil ditambahkan."
        return render(request, 'tambah-surat-rpl.html', {'msg':msg})
    else:
        siswa1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False)
        siswa2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False)
        siswa3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False)
        instansis = Instansi.objects.all()
        return render(request, 'tambah-surat-rpl.html',
            {'siswa1':siswa1, 'siswa2':siswa2, 'siswa3':siswa3, 'instansis':instansis}
        )

    return render(request, 'tambah-surat-rpl.html',
        {'siswa1':siswa1, 'siswa2':siswa2, 'siswa3':siswa3, 'instansis':instansis}
    )



@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_rpl(request):
    fix = Permohonan.objects.filter(nama_siswa__pkl=True, nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi__nama')
    return render(request, 'cetak-surat-rpl.html', {'surat':fix})

@login_required(login_url=settings.LOGIN_URL)
def cetak_rpl_belum_pkl(request):
    siswa = Siswa.objects.filter(pkl=False, program_ahli='Rekayasa Perangkat Lunak').order_by('NIS')
    count = siswa.count()
    return render(request, 'cetak-rpl-belum-pkl.html', {'siswa':siswa, 'count':count})


@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_tkj(request):
    fix = Permohonan.objects.filter(nama_siswa__pkl=True, nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi__nama')
    return render(request, 'cetak-surat-tkj.html', {'surat':fix})

@login_required(login_url=settings.LOGIN_URL)
def cetak_tkj_belum_pkl(request):
    siswa = Siswa.objects.filter(pkl=False, program_ahli='Teknik Komputer dan Jaringan').order_by('NIS')
    count = siswa.count()
    return render(request, 'cetak-tkj-belum-pkl.html', {'siswa':siswa, 'count':count})
