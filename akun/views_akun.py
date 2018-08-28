from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from akun.models import Akun

# Create your views here.
def akun_login(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(username=user.id)
                    login(request, user)
                    request.session['username'] = request.POST['username']
                    request.session['nama_depan'] = akun.nama_depan
                    request.session['nama_belakang'] = akun.nama_belakang
                    request.session['id'] = akun.id
                except:
                    messages.add_message(request, messages.INFO, 'Login Gagal :(')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'User tidak terdaftar.')
        else:
            messages.add_message(request, messages.INFO, 'Login gagal.')
    return render(request, 'login.html')

@login_required(login_url=settings.LOGIN_URL)
def akun_logout(request):
    logout(request)
    return redirect('/login/')
