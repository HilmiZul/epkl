import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from master.models import Instansi, InstansiTKJ

@login_required(login_url=settings.LOGIN_URL)
def export_instansi_tkj(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-TKJ.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Instansi.TKJ')

    row_num = 0
    columns = ['NAMA INSTANSI', 'ALAMAT',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    inst = InstansiTKJ.objects.all().order_by('nama').values_list('nama', 'alamat')
    for i in inst:
        row_num += 1
        for col_num in range(len(i)):
            ws.write(row_num, col_num, i[col_num])

    wb.save(response)
    return response

@login_required(login_url=settings.LOGIN_URL)
def export_instansi_rpl(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-RPL.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Instansi.RPL')

    row_num = 0
    columns = ['NAMA INSTANSI', 'ALAMAT',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    inst = Instansi.objects.all().order_by('nama').values_list('nama', 'alamat')
    for i in inst:
        row_num += 1
        for col_num in range(len(i)):
            ws.write(row_num, col_num, i[col_num])

    wb.save(response)
    return response
