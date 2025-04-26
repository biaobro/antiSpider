import string

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
import execjs
import random


# 返回服务器时间
def lesson1_server_time(request):
    return HttpResponse(int(time.time() * 1000))


def lesson1_01(request):
    # return HttpResponse("section02/lesson1")
    return render(request, "section02/lesson1_01.html")


def lesson1_01_data_api(request):
    token = request.COOKIES.get("token")
    key = "section02lesson1"
    with open("/AntiSpider/section02/utils/lesson1_decode.js", "r", encoding="utf-8") as file:
        result = execjs.compile(file.read()).call("decode", token, key)
    # print(result)

    # now time: 1745159783476
    # 以空格为基准拆分 result 得到最后的时间值
    _time = result.split(" ")[-1]

    # 如果前端的时间 与 服务端时间相差1s以内
    if abs(time.time() - int(_time) / 1000) <= 1:
        return JsonResponse({"code": "1"})
    else:
        return JsonResponse({"code": "2"})


def lesson1_02(request):
    return render(request, "section02/lesson1_02.html")


def lesson1_02_data_api(request):
    token = request.session.get("lesson1_02")
    page = request.GET.get("page")
    _key = token.split('|')[0] if token else "0"
    _value = token.split('|')[1] if token else "1"
    value = request.COOKIES.get(_key)

    if value == _value or int(page) == 1:
        _cookie_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        _cookie_value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        # _random_num = str(random.randint(1, 5000))
        request.session["lesson1_02"] = _cookie_key + '|' + _cookie_value
        # del request.session["set_1_02"]
        response = JsonResponse({"getTokenFromServer": page})
        response.set_cookie(_cookie_key, _cookie_value)
        return response
    else:
        return JsonResponse({"getTokenFromServer": "nothing "})


def lesson1_03(request):
    return render(request, "section02/lesson1_03.html")


def lesson1_03_data_api(request):
    return JsonResponse({"code": "1"})
