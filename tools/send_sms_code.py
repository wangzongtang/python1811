import random

import requests
from django.core.cache import cache

from common.keys import VCODE
from python1811.config import YZX_SMS_URL, YZX_SMS_PARAMS


def gene_code(length=4):  # 获取验证码
    start = 10 ** (length - 1)
    end = 10 ** length
    return random.randrange(start, end)


def send_sms(phone):  # 发送短信
    url = YZX_SMS_URL
    params = YZX_SMS_PARAMS.copy()
    code = gene_code()
    params['param'] = code
    cache.set(VCODE % phone, code, 300)
    params['mobile'] = phone

    response = requests.post(url=url, json=params)   # 发送短信
    if response.status_code == 200:                  # 判断请求是否发送成功
        result = response.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return False,'短信服务器通信出错'
