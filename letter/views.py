from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from master.models import Instansi, Siswa, InstansiTKJ
from letter.models import Permohonan, PermohonanTKJ
from pesan import pesan

# Create your views here.
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
        msg = pesan().update()
        surat = Permohonan.objects.get(id=id_surat)
        siswa1 = Siswa.objects.filter(kelas='XII.RPL-1')
        siswa2 = Siswa.objects.filter(kelas='XII.RPL-2')
        siswa3 = Siswa.objects.filter(kelas='XII.RPL-3')
        instansis = Instansi.objects.all()
        return render(request, 'ubah-surat-rpl.html',
            {
                'surat':surat,
                'msg':msg,
                'siswa1':siswa1,
                'siswa2':siswa2,
                'siswa3':siswa3,
                'instansis':instansis,
            }
        )
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
def ubah_surat_tkj(request,id_surat):
    if request.POST:
        s = Siswa.objects.get(id=request.POST['nama_siswa'])
        i = InstansiTKJ.objects.get(id=request.POST['nama_instansi'])

        PermohonanTKJ.objects.filter(id=id_surat).update(
            nama_siswa = s,
            nama_instansi = i,
        )
        msg = pesan().update()
        siswa1 = Siswa.objects.filter(kelas='XII.TKJ-1')
        siswa2 = Siswa.objects.filter(kelas='XII.TKJ-2')
        siswa3 = Siswa.objects.filter(kelas='XII.TKJ-3')
        siswa4 = Siswa.objects.filter(kelas='XII.TKJ-4')
        instansis = InstansiTKJ.objects.all()
        surat = PermohonanTKJ.objects.get(id=id_surat)
        return render(request, 'ubah-surat-tkj.html',
            {
                'msg':msg,
                'surat':surat,
                'siswa1':siswa1,
                'siswa2':siswa2,
                'siswa3':siswa3,
                'siswa4':siswa4,
                'instansis':instansis,
            }
        )
    else:
        surat = PermohonanTKJ.objects.get(id=id_surat)
        siswa1 = Siswa.objects.filter(kelas='XII.TKJ-1')
        siswa2 = Siswa.objects.filter(kelas='XII.TKJ-2')
        siswa3 = Siswa.objects.filter(kelas='XII.TKJ-3')
        siswa4 = Siswa.objects.filter(kelas='XII.TKJ-4')
        instansis = InstansiTKJ.objects.all()
    return render(request, 'ubah-surat-tkj.html',
        {
            'surat':surat,
            'siswa1':siswa1,
            'siswa2':siswa2,
            'siswa3':siswa3,
            'siswa4':siswa4,
            'instansis':instansis,
        }
    )



@login_required(login_url=settings.LOGIN_URL)
def surat_tkj(request):
    surat = PermohonanTKJ.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi')
    return render(request, 'surat-tkj.html', {'surats':surat})


# HAPUS.TKJ
@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_tkj(request, id_surat):
    if request.POST:
        # ambil dulu ID Siswa dari model Permohonan
        id_siswa = PermohonanTKJ.objects.get(id=id_surat)
        Siswa.objects.filter(id=id_siswa.nama_siswa.id).update(pkl = False)
        # lalu hapus data surat permohonannya
        PermohonanTKJ.objects.filter(id=id_surat).delete()
        msg = pesan().delete()
        get_surat = PermohonanTKJ.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
    else:
        return redirect('/surat-tkj/')
    return render(request, 'surat-tkj.html', {'msg':msg, 'surat':get_surat})


# HAPUS.RPL
@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_rpl(request, id_surat):
    if request.POST:
        id_siswa = Permohonan.objects.get(id=id_surat)
        Siswa.objects.filter(id=id_siswa.nama_siswa.id).update(pkl = False)
        Permohonan.objects.filter(id=id_surat).delete()
        msg = pesan().delete()
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
        instansi = InstansiTKJ.objects.get(id=request.POST['nama_instansi'])
        PermohonanTKJ(
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
        instansis = InstansiTKJ.objects.all()
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
