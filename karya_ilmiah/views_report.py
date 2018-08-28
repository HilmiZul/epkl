import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from karya_ilmiah.models import KaryaIlmiah

@login_required(login_url=settings.LOGIN_URL)
def report_karil_tkj(request):
    karil_tkj = KaryaIlmiah.objects.filter(nama__kelas__contains="XII.TKJ").order_by('nama__kelas', 'nama')
    jumlah = karil_tkj.count()
    return render(request, 'report-karil-tkj.html', {'karil_tkj': karil_tkj, 'jumlah': jumlah})

@login_required(login_url=settings.LOGIN_URL)
def report_karil_rpl(request):
    karil_rpl = KaryaIlmiah.objects.filter(nama__kelas__contains="XII.RPL").order_by('nama__kelas', 'nama')
    jumlah = karil_rpl.count()
    return render(request, 'report-karil-rpl.html', {'karil_rpl': karil_rpl, 'jumlah':jumlah})


# EXPORT SEMUA KARYA ILMIAH TKJ & RPL KE FILE .xls
# Haturnuhun ka Kang Vitor Freitas
# reference: https://simpleisbetterthancomplex.com/tutorial/2016/07/29/how-to-export-to-excel.html
@login_required(login_url=settings.LOGIN_URL)
def export_karil_tkj(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Karya-Ilmiah-XII.TKJ.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Karil.TKJ')

    row_num = 0
    columns = ['JUDUL', 'TANGGAL ACC.', 'PEMBIMBING', 'NAMA SISWA', 'KELAS', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    karil = KaryaIlmiah.objects.filter(nama__kelas__contains='XII.TKJ').order_by('nama__kelas', 'nama__nama').values_list('judul', 'tanggal_acc', 'pembimbing__nama', 'nama__nama', 'nama__kelas')
    for k in karil:
        row_num += 1
        for col_num in range(len(k)):
            ws.write(row_num, col_num, k[col_num])

    wb.save(response)
    return response

@login_required(login_url=settings.LOGIN_URL)
def export_karil_rpl(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Karya-Ilmiah-XII.RPL.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Karil.RPL')

    row_num = 0
    columns = ['JUDUL', 'TANGGAL ACC.', 'PEMBIMBING', 'NAMA SISWA', 'KELAS', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    karil = KaryaIlmiah.objects.filter(nama__kelas__contains='XII.RPL').order_by('nama__kelas', 'nama__nama').values_list('judul', 'tanggal_acc', 'pembimbing__nama', 'nama__nama', 'nama__kelas')
    for k in karil:
        row_num += 1
        for col_num in range(len(k)):
            ws.write(row_num, col_num, k[col_num])

    wb.save(response)
    return response
