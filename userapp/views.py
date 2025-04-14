from django.shortcuts import render

# Create your views here.



def createUserGet(request):
    return render(request, "userapp/create.html")


def createUserPost(request):
#     newUser = User()
# #    newUser.user_id = request.POST.get('user_id', None)
#     newUser.username = request.POST.get('username', None)
#     newUser.password = request.POST.get('password',    None)
#     newUser.email = request.POST.get('email', None)
#     newUser.created_at = request.POST.get('created_at', None)
#     newUser.save()

    return render(request, "accountapp/result.html")

def readUserGet(request):
    return render(request, "accountapp/list.html")
