import email
from tempfile import mkdtemp
from django.shortcuts import render

from dangky.models import NguoiDung


# Create your views here.

def dangky(request):
    return render(request,'dangky.html')

def trangchu(request):
    return render(request,'trangchu.html')

def xuly_dangky(request):
    ten = request.GET.get('ten')
    email = request.GET.get('mail')
    mk = request.GET.get('matkhau')
    if(len(ten) <10):
        return render(request,'loi.html')
    else:
        dulieu = NguoiDung(
            ten_dang_nhap = ten,
            email = email,
            mat_khau = mk
        )
        dulieu.save()
        return render(request, 'dangnhap.html')
