from django.shortcuts import render


# Create your views here.
from stu.models import LoginUser


def show(request):
    userlist = LoginUser.objects.all()
    print(userlist)
    return render(request, 'abc.html', {'users': userlist})
