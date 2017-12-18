from django.shortcuts import render,redirect
from .models import UserInfo
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect


def login(request):
    username = request.COOKIES.get('username', '')
    context = {
        'error_name': 0,
        'error_pwd': 0,
        'username': username,
    }
    return render(request,'user/login.html', context)

def login_handle(request):
    post = request.POST
    userphone = post.get('userphone')
    userpassword = post.get('userpassword')
    users = UserInfo.objects.filter(userphone=userphone)
    if len(users) == 1:
        print(userphone)
        s1 = sha1()
        s1.update(str(userpassword).encode('utf-8'))
        if s1.hexdigest() == users[0].userpassword:
            url = request.COOKIES.get('url', '/')  # 从cookie中取出url完整路径参照user_decorator
            red = HttpResponseRedirect(url)
            request.session['user_id'] = users[0].id  # 用于user_decorator传用户id验证是否登录
            request.session['userphone'] = userphone
            return red
        else:
            context = { 'error_phone': 0, 'error_pwd': 1, 'userphone': userphone,
                       'userpassword': userpassword}
            return render(request, 'user/login.html', context)
    else:
        context = { 'error_phone': 1, 'error_pwd': 0, 'userphone': userphone, 'userpassword': userpassword}
        return render(request, 'user/login.html', context)

def  register(request):
   return render(request, 'user/register.html')

def register_handle(request):
    post = request.POST
    username = post.get('userphone')
    userphone = post.get('userphone')
    userpassword=post.get('userpassword')
#    cuserpassword = post.get('cpwd')
#    if userpassword != cuserpassword:
 #       return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(str(userpassword).encode('utf-8'))
    upwd = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.userphone= userphone
    user.username = username
    print(username)
    user.userpassword = upwd
    user.save()
    return redirect('/user/login/')



