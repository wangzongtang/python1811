from django.core.cache import cache

from common import status
from common.keys import VCODE
from tools.forms import ProfileForm
from tools.http_json import render_json
from tools.send_sms_code import send_sms
from user.models import User


def get_phone(request):                       # 获取手机号,通过手机号码发送短信
    times = 3
    phonenum = request.POST.get('phone')
    while times > 0:                         # 三次重试
        result = send_sms(phonenum)          # 发送短信
        if result[0]:
            break
        else:
            times -= 1
    return render_json(data='successful', code=status.SUCCESS_CODE)


def submit_vcode(request):                    # 通过验证码登录、注册
    phonenum = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    cache_code = cache.get(VCODE % phonenum)  # 从缓存中获取验证码

    if vcode == str(cache_code):
        user, _ = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        return render_json(data=user.to_dict(), code=status.SUCCESS_CODE)
    else:
        return render_json(data='验证码错误', code=status.SMS_ERROR)


def get_profile(request):   # 获取个人资料
    user = User.objects.get(id=request.session['uid'])
    return render_json(user.profile.to_dict())


def edit_profile(request):   # 修改个人资料
    profile_form = ProfileForm(request.POST)   # 通过form表单,获取数据
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.id = request.session['uid']
        profile.save()
        return render_json(profile.to_dict())
    else:
        return render_json(profile_form.errors, status.PROFILE_ERR)


def up_load(request):    # 头像上传
    pass

