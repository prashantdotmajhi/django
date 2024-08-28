from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')


def singup(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password == re_password:
            user = User.objects.create_user(first_name = first_name,last_name=last_name,username=email,email=email,password=password)
            user.save()
            return render(request,'Sing_up.html',{"message":"User created Sucessfilly!!!"})

        else:
            return render(request,'Sing_up.html',{"error":"Password didn't match!!!"})

    return render(request,'Sing_up.html')

def login(request):
    return render(request,'login.html')
