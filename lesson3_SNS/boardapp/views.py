from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required

# Create your views here.
#ユーザー登録
def signupfunc(request):
    if request.method == 'POST':#POSTとしてデータが送信されたときにサインアップさせる
        uname = request.POST['username']
        pword = request.POST['password']
        try:
            User.objects.get(username=uname)
            return render(request,'signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(uname,'',pword)
            return render(request,'signup.html',{'some':100})
    return render(request,'signup.html')

#render     ：指定されたページに移動する                 =>URLが変わらない
#redirect   ：指定されたURLを呼び出して、リダイレクトする   =>URLが変わる

def loginfunc(request):
    if request.method == 'POST':#POSTとしてデータが送信されたときにサインアップさせる
        uname = request.POST['username']
        pword = request.POST['password']
        user = authenticate(request,username=uname,password=pword)
        if user is not None:#ユーザーが存在する場合
            login(request,user)
            #return render(request,'signup.html',{'error':"ログインできました"})
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')

#サインアウトしていた時にlistにアクセスしたらloginにアクセスする
#settings.py => LOGIN_URL = 'login'
@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')