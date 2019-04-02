from django.conf.urls import url

from user import api

urlpatterns = [
    url(r'^getCode/$', api.get_phone, name='getCode'),            # 获取验证码
    url(r'^getUser/$', api.submit_vcode, name='getUser'),            # 登录或注册
    url(r'^getProfile/$', api.get_profile, name='getProfile'),           # 获取个人资料
    url(r'^editProfile/$', api.edit_profile, name='editProfile')       # 修改个人资料
]
