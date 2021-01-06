from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .form import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    else:
        return HttpResponse('home')
def loout(request):
    if request.session.get('user'):
        del(request.session['user'])
        
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            ## session 처리
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password',None)
        repassword = request.POST.get('repassword',None)

        res_data = {}
        # 빈문자열일 경우 거짓. None일 경우 거짓. 모든 값이 true 가 아니면.
        if not (username and useremail and password and repassword):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != repassword :
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(username  = username,
                            useremail = useremail,
                            password  = make_password(password))
            fcuser.save()
        return render(request, 'register.html',res_data)
