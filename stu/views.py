from django.shortcuts import render


# Create your views here.
from stu.models import LoginUser


def show(request):
    userlist = LoginUser.objects.all()
    return render(request, 'abc.html', {'users': userlist})
