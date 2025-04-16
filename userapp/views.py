from django.shortcuts import render

from userapp.models import ZUser

from django.contrib.auth.hashers import make_password, check_password


# Create your views here.



def createUserGet(request):
    return render(request, "userapp/create.html")


def createUserPost(request):
    user = ZUser()
    user.id = request.POST.get('email', None)
    user.name = request.POST.get('name', None)

    password = request.POST.get('password', None)
    hashed_password = make_password(password)

    user.password = hashed_password;
    user.inuse = True
    user.email = request.POST.get('email', None)
    user.save()

    # from django.contrib.auth.hashers import make_password, check_password
    #
    # # 비밀번호 해싱 – 데이터베이스에 저장할 때
    # raw_password = 'password123'
    # hashed_password = make_password(raw_password)
    # print(f"Hashed Password: {hashed_password}")
    #
    # # 비밀번호 검증 – 로그인 시 입력된 비밀번호가 올바른지 확인할 때
    # is_valid = check_password('password123', hashed_password)
    # print(f"Password is valid? {is_valid}")

    return render(request, "userapp/result.html")

def readUserGet(request):
    return render(request, "userapp/list.html")
