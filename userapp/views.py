from django.shortcuts import render

from userapp.models import ZUser


# Create your views here.



def createUserGet(request):
    return render(request, "userapp/create.html")


def createUserPost(request):
    user = ZUser()
    user.id = request.POST.get('email', None)
    user.name = request.POST.get('name', None)
    user.password = request.POST.get('password', None)
    user.inuse = True
    user.email = request.POST.get('email', None)
    user.save()

    return render(request, "userapp/result.html")

def readUserGet(request):
    return render(request, "userapp/list.html")
