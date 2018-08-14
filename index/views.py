from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import *


# Create your views here.
def index_views(request):
    return render(request, 'main.html', {})


def login_views(request):
    if request.method == 'GET':
        # 用户访问登录路径时，判断session中是否存在登陆信息
        if 'uphone' in request.session and 'password' in request.session:
            return HttpResponseRedirect('/index/')
        else:
            # 用户访问登录路径时，判断cookies中是否存在登陆信息
            if 'uphone' in request.COOKIES and 'password' in request.COOKIES:
                # 从cookies中获取手机号和密码
                uphone = request.COOKIES['uphone']
                password = request.COOKIES['password']
                # 将手机号和密码保存进session
                request.session['uphone'] = uphone
                request.session['password'] = password
                # 重定向到index页面
                return HttpResponseRedirect('/index/')
            else:
                # 登陆信息不存在则用户进入登录页面
                return render(request, 'login.html', {})
    else:
        # 用户处理登录信息，验证登录内容
        # 从前端获取手机号和密码
        upon = request.POST['upon']
        upwd = request.POST['upwd']
        # 搜索数据库，与request中的信息进行比对
        user = User.objects.filter(uphone=upon, password=upwd)
        if user:
            # 将手机号和密码保存进session
            request.session['uphone'] = upon
            request.session['password'] = upwd
            # 判断是否勾选记住密码
            if 'isSaved' in request.POST:
                # 将登录者的ID和手机号保存进cookie,重定向到index页面
                resp = HttpResponseRedirect('/index/')
                resp.set_cookie('uphone', user[0].uphone, 60 * 60 * 24 * 365)
                resp.set_cookie('password', user[0].password, 60 * 60 * 24 * 365)
                return resp
            return HttpResponseRedirect('/index/')
        else:
            # 匹配不到用户信息提示错误信息
            return render(request, 'login.html', {'error': '账号或密码输入错误'})


def register_views(request):
    if request.method == 'GET':
        # 用户进入注册页面
        return render(request, 'register.html', {})
    else:
        # 用户处理登录信息，验证登录内容
        # 从前端获取的手机号、密码、用户名、邮箱
        upon = request.POST.get('upon', '')
        # 判断用户输入的手机号格式是否正确
        if len(upon) == 11 and type(upon) == int:
            # 搜索数据库，获取用户所有用户手机号信息，与request中的信息进行比对
            user = User.objects.filter(uphone=upon)
            if user:
                # 如果手机号在数据库中已经存在，提示用户已存在，重新注册
                return render(request, 'register.html', {'error': 2})
            else:
                upwd = request.POST['upwd1']
                uname = request.POST['uname']
                uemail = request.POST['uemail']
                if len(upwd) >= 6 or len(upwd) <= 20:
                    dic = {
                        'uphone': upon,
                        'password': upwd,
                        'uname': uname,
                        'email': uemail,
                    }
                    obj = User(**dic)
                    obj.save()
                    # 注册成功转发到登录页面
                    return HttpResponseRedirect('/login/')
                else:
                    return render(request, 'register.html', {'error': 1})
        else:
            # 手机号输入有误
            return render(request, 'register.html', {'error': 3})

