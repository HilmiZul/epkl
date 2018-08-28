import xlwt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from master.models import Instansi, Siswa, InstansiTKJ
from letter.models import Permohonan, PermohonanTKJ


# LAPORAN PERMOHONAN PKL
@login_required(login_url=settings.LOGIN_URL)
def laporan_permohonan(request):
    permohonan = Permohonan.objects.all().order_by('nama_instansi')
    return render(request, 'laporan.html', {'permohonans':permohonan})


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

def form_cetak_tkj(request,id_ins):
    if id_ins is not None:
        meta_surat = PermohonanTKJ.objects.filter(nama_instansi_id=id_ins)
        instansi = InstansiTKJ.objects.get(id=id_ins)
        result = render(request, 'cetak.html', {'meta_surat':meta_surat, 'instansi':instansi})
    else:
        result = redirect('/')
    return result

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
    fix = PermohonanTKJ.objects.filter(nama_siswa__pkl=True, nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi__nama')
    return render(request, 'cetak-surat-tkj.html', {'surat':fix})

@login_required(login_url=settings.LOGIN_URL)
def cetak_tkj_belum_pkl(request):
    siswa = Siswa.objects.filter(pkl=False, program_ahli='Teknik Komputer dan Jaringan').order_by('NIS')
    count = siswa.count()
    return render(request, 'cetak-tkj-belum-pkl.html', {'siswa':siswa, 'count':count})



# EXPORT TEMPAT SISWA PKL KE XLS
# RPL
@login_required(login_url=settings.LOGIN_URL)
def export_pkl_rpl(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Instansi-XII.RPL.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Instansi.RPL')

    row_num = 0
    columns = ['INSTANSI', 'ALAMAT', 'NAMA SISWA', 'KELAS', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    pkl = Permohonan.objects.filter(nama_siswa__pkl=True, nama_siswa__kelas__contains='XII.RPL').order_by(
                'nama_instansi', 'nama_siswa__kelas', 'nama_siswa__nama'
            ).values_list(
                'nama_instansi__nama', 'nama_instansi__alamat', 'nama_siswa__nama', 'nama_siswa__kelas'
            )
    for p in pkl:
        row_num += 1
        for col_num in range(len(p)):
            ws.write(row_num, col_num, p[col_num])

    wb.save(response)
    return response

# TKJ
@login_required(login_url=settings.LOGIN_URL)
def export_pkl_tkj(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Instansi-XII.TKJ.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Instansi.TKJ')

    row_num = 0
    columns = ['INSTANSI', 'ALAMAT', 'NAMA SISWA', 'KELAS', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    pkl = PermohonanTKJ.objects.filter(nama_siswa__pkl=True, nama_siswa__kelas__contains='XII.TKJ').order_by(
                'nama_instansi', 'nama_siswa__nama', 'nama_siswa__kelas'
            ).values_list(
                'nama_instansi__nama', 'nama_instansi__alamat', 'nama_siswa__nama', 'nama_siswa__kelas'
            )
    for p in pkl:
        row_num += 1
        for col_num in range(len(p)):
            ws.write(row_num, col_num, p[col_num])

    wb.save(response)
    return response
