from django.shortcuts import render
import time
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def v_help(request):

    return render(request, 'v_help.html')


def login(request, message=''):
    res = {}
    res["message"] = message

    return render(request,'login.html', res)


def login_action(request):
    time.sleep(1)
    # 获取用户名/密码
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    # 去数据库中比对
    user = auth.authenticate(username=username, password=password)
    # 失败，弹出提示
    if user is None:
        return login(request, '用户名或密码错误')
    else:  # 成功，跳转到首页
        if username=='admin':
            return HttpResponseRedirect('/admin/')
        else:
            # 登录
            auth.login(request, user)
            request.session['user'] = username
            return HttpResponseRedirect('/help/')
