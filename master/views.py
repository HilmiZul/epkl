from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from master.models import Siswa, Instansi, InstansiTKJ
from master.forms import FormAddTKJ, FormAddRPL

# Create your views here.

# TKJ
@login_required(login_url=settings.LOGIN_URL)
def master_tkj(request):
    master = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan').order_by('kelas')
    return render(request, 'master-tkj.html', {'master':master})

# ADD.TKJ
@login_required(login_url=settings.LOGIN_URL)
def add_master_tkj(request):
    if request.POST:
        form = FormAddTKJ(request.POST)
        if form.is_valid():
            add_siswa = Siswa(
                NIS = request.POST['NIS'],
                nama = request.POST['nama'],
                kelas = request.POST['kelas'],
                program_ahli = 'Teknik Komputer dan Jaringan',
            ).save()

            msg = "Berhasil ditambahkan."
            form = FormAddTKJ()
            return render(request, 'add-master-tkj.html', {'msg':msg, 'form':form})
    else:
        form = FormAddTKJ()
    return render(request, 'add-master-tkj.html', {'form':form})

# TKJ-1
# SHOW.ALL
@login_required(login_url=settings.LOGIN_URL)
def master_tkj_1(request):
    master = Siswa.objects.filter(kelas='XII.TKJ-1').order_by('kelas')
    return render(request, 'master-tkj-1.html', {'master':master})

# UBAH.TKJ
@login_required(login_url=settings.LOGIN_URL)
def ubah_tkj_1(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-tkj-1.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-tkj-1.html', {'siswa':siswa_update})

@login_required(login_url=settings.LOGIN_URL)
def ubah_tkj_2(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-tkj-2.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-tkj-2.html', {'siswa':siswa_update})

@login_required(login_url=settings.LOGIN_URL)
def ubah_tkj_3(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-tkj-3.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-tkj-3.html', {'siswa':siswa_update})

@login_required(login_url=settings.LOGIN_URL)
def ubah_tkj_4(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-tkj-4.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-tkj-4.html', {'siswa':siswa_update})


# DELETE.TKJ
@login_required(login_url=settings.LOGIN_URL)
def delete_tkj_1(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-tkj-1/')

# TKJ-2
# SHOW.ALL
@login_required(login_url=settings.LOGIN_URL)
def master_tkj_2(request):
    master = Siswa.objects.filter(kelas='XII.TKJ-2').order_by('kelas')
    return render(request, 'master-tkj-2.html', {'master':master})

# DELETE.TKJ
@login_required(login_url=settings.LOGIN_URL)
def delete_tkj_2(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-tkj-2/')


# TKJ-3
# SHOW.ALL
@login_required(login_url=settings.LOGIN_URL)
def master_tkj_3(request):
    master = Siswa.objects.filter(kelas='XII.TKJ-3').order_by('kelas')
    return render(request, 'master-tkj-3.html', {'master':master})

# DELETE
@login_required(login_url=settings.LOGIN_URL)
def delete_tkj_3(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-tkj-3/')


# TKJ-4
# SHOW.ALL
@login_required(login_url=settings.LOGIN_URL)
def master_tkj_4(request):
    master = Siswa.objects.filter(kelas='XII.TKJ-4').order_by('kelas')
    return render(request, 'master-tkj-4.html', {'master':master})

# DELETE.TKJ
@login_required(login_url=settings.LOGIN_URL)
def delete_tkj_4(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-tkj-4/')


##
# RPL
@login_required(login_url=settings.LOGIN_URL)
def master_rpl(request):
    master = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak').order_by('kelas')
    return render(request, 'master-rpl.html', {'master':master})

# ADD
@login_required(login_url=settings.LOGIN_URL)
def add_master_rpl(request):
    if request.POST:
        form = FormAddRPL(request.POST)
        if form.is_valid():
            add_siswa = Siswa(
                NIS = request.POST['NIS'],
                nama = request.POST['nama'],
                kelas = request.POST['kelas'],
                program_ahli = 'Rekayasa Perangkat Lunak',
            ).save()

            msg = "Berhasil ditambahkan."
            form = FormAddRPL()
            return render(request, 'add-master-rpl.html', {'msg':msg, 'form':form})
    else:
        form = FormAddRPL()
    return render(request, 'add-master-rpl.html', {'form':form})


# UBAH.RPL
@login_required(login_url=settings.LOGIN_URL)
def ubah_rpl_1(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-rpl-1.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-rpl-1.html', {'siswa':siswa_update})

@login_required(login_url=settings.LOGIN_URL)
def ubah_rpl_2(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-rpl-2.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-rpl-2.html', {'siswa':siswa_update})

@login_required(login_url=settings.LOGIN_URL)
def ubah_rpl_3(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).update(
            nama = request.POST['nama'],
            kelas = request.POST['kelas'],
        )
        msg = "Berhasil diperbaharui."
        siswa_update = Siswa.objects.get(id=id_siswa)
        return render(request, 'ubah-rpl-3.html', {'msg':msg, 'siswa':siswa_update})
    else:
        siswa_update = Siswa.objects.get(id=id_siswa)
    return render(request, 'ubah-rpl-3.html', {'siswa':siswa_update})


# RPL-1
# SHOW.ALL
@login_required(login_url=settings.LOGIN_URL)
def master_rpl_1(request):
    master = Siswa.objects.filter(kelas='XII.RPL-1').order_by('kelas')
    return render(request, 'master-rpl-1.html', {'master':master})

@login_required(login_url=settings.LOGIN_URL)
def master_rpl_2(request):
    master = Siswa.objects.filter(kelas='XII.RPL-2').order_by('kelas')
    return render(request, 'master-rpl-2.html', {'master':master})

@login_required(login_url=settings.LOGIN_URL)
def master_rpl_3(request):
    master = Siswa.objects.filter(kelas='XII.RPL-3').order_by('kelas')
    return render(request, 'master-rpl-3.html', {'master':master})

# DELETE.RPL
@login_required(login_url=settings.LOGIN_URL)
def delete_rpl_1(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-rpl-1/')

@login_required(login_url=settings.LOGIN_URL)
def delete_rpl_2(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-rpl-2/')

@login_required(login_url=settings.LOGIN_URL)
def delete_rpl_3(request,id_siswa):
    if request.POST:
        Siswa.objects.filter(id=id_siswa).delete()
    return redirect('/master-rpl-3/')



################################################################
#
# INTANSI

# RPL
@login_required(login_url=settings.LOGIN_URL)
def master_instansi_rpl(request):
    master = Instansi.objects.all().order_by('nama')
    return render(request, 'master-instansi-rpl.html', {'master':master})

@login_required(login_url=settings.LOGIN_URL)
def add_instansi_rpl(request):
    if request.POST:
        Instansi(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
        ).save()
        msg = "Berhasil ditambahkan."
        return render(request, 'add-instansi-rpl.html', {'msg':msg})
    return render(request, 'add-instansi-rpl.html')

# INSTANSI.HAPUS
@login_required(login_url=settings.LOGIN_URL)
def delete_instansi_rpl(request,id_instansi):
    if request.POST:
        Instansi.objects.filter(id=id_instansi).delete()
        msg = "Berhasil dihapus."
        get_instansi = Instansi.objects.all()
    else:
        return redirect('/master-instansi/rpl')
    return render(request, 'master-instansi-rpl.html', {'msg':msg, 'master':get_instansi})

@login_required(login_url=settings.LOGIN_URL)
def ubah_instansi_rpl(request,id_instansi):
    if request.POST:
        Instansi.objects.filter(id=id_instansi).update(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
        )
        msg = "Berhasil diperbaharui."
        instansi = Instansi.objects.get(id=id_instansi)
        return render(request, 'ubah-instansi-rpl.html', {'msg':msg, 'instansi':instansi})
    else:
        instansi = Instansi.objects.get(id=id_instansi)
    return render(request, 'ubah-instansi-rpl.html', {'instansi':instansi})


################################################################
# TKJ
@login_required(login_url=settings.LOGIN_URL)
def master_instansi_tkj(request):
    master = InstansiTKJ.objects.all().order_by('nama')
    return render(request, 'master-instansi-tkj.html', {'master':master})

@login_required(login_url=settings.LOGIN_URL)
def add_instansi_tkj(request):
    if request.POST:
        InstansiTKJ(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
        ).save()
        msg = "Berhasil ditambahkan."
        return render(request, 'add-instansi-tkj.html', {'msg':msg})
    return render(request, 'add-instansi-tkj.html')

@login_required(login_url=settings.LOGIN_URL)
def delete_instansi_tkj(request,id_instansi):
    if request.POST:
        InstansiTKJ.objects.filter(id=id_instansi).delete()
        msg = "Berhasil dihapus."
        get_instansi = InstansiTKJ.objects.all()
    else:
        return redirect('/master-instansi/tkj')
    return render(request, 'master-instansi-tkj.html', {'msg':msg, 'master':get_instansi})

@login_required(login_url=settings.LOGIN_URL)
def ubah_instansi_tkj(request,id_instansi):
    if request.POST:
        InstansiTKJ.objects.filter(id=id_instansi).update(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
        )
        msg = "Berhasil diperbaharui."
        instansi = InstansiTKJ.objects.get(id=id_instansi)
        return render(request, 'ubah-instansi-tkj.html', {'msg':msg, 'instansi':instansi})
    else:
        instansi = InstansiTKJ.objects.get(id=id_instansi)
    return render(request, 'ubah-instansi-tkj.html', {'instansi':instansi})

#
################################################################




##
# ABSENSI
@login_required(login_url=settings.LOGIN_URL)
def absensi(request):
    return render(request, 'absensi.html')

@login_required(login_url=settings.LOGIN_URL)
def cetak_absensi(request):
    if request.POST:
        judul = request.POST['judul']
        kelas = request.POST['get_kelas']
        siswa = Siswa.objects.filter(kelas=kelas)
    else:
        return redirect('/absensi/')
    return render(request, 'cetak-absensi.html', {'siswa':siswa, 'kelas':kelas, 'judul':judul})




@login_required(login_url=settings.LOGIN_URL)
def cetak_instansi(request):
    instansi = Instansi.objects.all()
    return render(request, 'cetak-instansi.html', {'instansi':instansi})
