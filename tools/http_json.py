"""
返回json数据
"""
import json

from django.conf import settings
from django.http import HttpResponse


def render_json(data, code=0):
    info = {
        'data': data,
        'code': code
    }

    if settings.DEBUG:
        result = json.dumps(info, ensure_ascii=False, indent=4)
    else:
        result = json.dumps(info, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(result)
