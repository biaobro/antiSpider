import json
import string

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
import execjs
import random
import json


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
    token = request.COOKIES.get("token")

    if token:
        print("get token")
        # 对 token 解密，得到时间值
        key = "section02lesson1"
        with open("/AntiSpider/section02/utils/lesson1_decode.js", "r", encoding="utf-8") as file:
            result = execjs.compile(file.read()).call("decode", token, key)

        # now time: 1745159783476
        # 以空格为基准拆分 result 得到最后的时间值
        _time = result.split(" ")[-1]
        print("_time", _time)
        print("time.time()", time.time())
        # 如果前端的时间 与 服务端时间相差1s以内
        if abs(time.time() - int(_time) / 1000) <= 100:
            return render(request, "section02/lesson1_03.html")

    print("not get token")
    # 如果鉴权不通过，返回 js
    # 如果鉴权通过，返回 html
    # html 中是script ，浏览器会执行 script，把 token 设置到 cookie 中
    with open("/AntiSpider/section02/utils/lesson1_3_cookie_anti_spider.html", encoding="utf-8") as f:
        return HttpResponse(f.read())


def lesson1_03_data_api(request):
    return JsonResponse({"code": "success"})


def lesson2_01(request):
    return render(request, "section02/lesson2_01.html")


from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt  # 关闭CSRF校验
@require_http_methods(["LINK"])  # 限制只接受LINK请求
def lesson2_01_data_api(request):
    def xorEncryptDecrypt(_input, _key):
        output = b""
        for i in range(len(_input)):
            charCode = _input[i]  # 输入就是字节码，所以直接遍历，不需要再用 ord()转换
            keyChar = _key[i % len(_key)]
            keyCharCode = ord(keyChar)
            encryptedCharCode = charCode ^ keyCharCode
            output += chr(encryptedCharCode).encode()
        return output

    key = "section02_lesson2_01"
    decrypt = xorEncryptDecrypt(request.body, key).decode()
    _page = int(decrypt[:-13])
    _timeStamp = int(decrypt[-13:])

    # 构造返回值，对返回值也进行加密

    respEncrypt = xorEncryptDecrypt(json.dumps({"code": _page}).encode(), key + "_response")
    print('backend:', respEncrypt)
    if abs(time.time() - int(_timeStamp) / 1000) <= 100:
        # 返回原文
        # return JsonResponse({"code": _page})

        # 返回密文
        return HttpResponse({respEncrypt})
    else:
        return JsonResponse({"code": "error"})


def lesson3_01(request):
    return render(request, "section02/lesson3_01.html")


@csrf_exempt
def lesson3_01_data_api(request):
    # print(request.body)
    from static.section02 import lesson3_01_pb2

    # 验证导入成功
    # print(lesson3_01_pb2)

    def xorEncryptDecrypt(_input, _key):
        output = b""
        for i in range(len(_input)):
            charCode = _input[i]  # 输入就是字节码，所以直接遍历，不需要再用 ord()转换
            keyChar = _key[i % len(_key)]
            keyCharCode = ord(keyChar)
            encryptedCharCode = charCode ^ keyCharCode
            output += chr(encryptedCharCode).encode()
        return output

    # 后端执行反序列化
    sec2_data = lesson3_01_pb2.msg()
    sec2_data.ParseFromString(request.body)
    key = sec2_data.key
    time = sec2_data.time
    page = sec2_data.page
    print(key, time, page)

    result = xorEncryptDecrypt(json.dumps({"code": page}).encode(), key)

    return HttpResponse(result)


def tls_check(request):
    from django.conf import settings

    # 兼容测试环境 直接返回True, 只有正式环境通过https访问的可以拿到指纹
    if settings.DEBUG:
        return True

    ssl_curves = request.environ.get("ssl_curves")
    print("ssl_curves : " + ssl_curves)
    if "secp384r1" not in ssl_curves:
        return False

    ssl_ciphers = request.environ.get("ssl_ciphers")
    print("ssl_ciphers : " + ssl_ciphers)
    if len(ssl_ciphers) != 355:
        return False

    http2_fingerprint = request.environ.get("http2_fingerprint")
    print("http2_fingerprint : " + http2_fingerprint)
    if "1:65536;2:0;4:6291456;6:262144|15663105|1:1:0:256|m,a,s,p" != http2_fingerprint:
        return False

    return True


def lesson4_01(request):
    # nginx_environ_list = ["ssl_ciphers", "ssl_curves", "ssl_protocol", "ssl_ja3", "ssl_ja3_hash", "http2_fingerprint", "ssl_ja4"]
    # return JsonResponse({i: request.environ.get(i) for i in nginx_environ_list})
    return render(request, "section02/lesson4_01.html")


@csrf_exempt  # 关闭默认的csrf校验
def lesson4_01_data_api(request):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    import base64

    # 后端过来的数据默认是经过base64编码的
    secureData = request.POST.get("secureData")

    # 字符串转换成字节
    bsecureData = secureData.encode()

    # "sec2-lesson4-key" 和前端加密的key一致
    aes = AES.new(b"sec2-lesson4-key", AES.MODE_ECB)

    # decode 是把字节再转换为字符串
    result = unpad(aes.decrypt(base64.b64decode(bsecureData)), 16).decode()
    print(result)

    page = int(result.split("|")[0])
    timeStamp = int(result.split("|")[1])

    # 得到的是10位时间戳
    currtime = time.time()
    print(currtime)

    if abs(currtime - timeStamp / 1000) < 2 and tls_check(request):
        # 用json 数据文件模拟读取数据库
        with open("/AntiSpider/section02/utils/data.json") as f:
            return JsonResponse(json.loads(f.read())["pages"][page - 1])
    else:
        with open("/AntiSpider/section02/utils/error.json") as f:
            return JsonResponse(json.loads(f.read()))
