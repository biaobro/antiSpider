from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time


# Create your views here.
def lesson3_01(request):
    # 渲染 templates 目录下的 html 文件
    return render(request, "section01/lesson3.html")


def lesson3_02(request):
    if request.GET.get('token') == 'aaaaa':
        return JsonResponse({'status': 200}, status=200)
    return JsonResponse({'status': 403}, status=403)


def lesson4_01(request):
    print(request.META)
    # print([header_list for header_list in request.META])

    # 标准、要求、设定的请求头顺序
    standard_headers = ['HTTP_HOST', 'HTTP_USER_AGENT', 'HTTP_ACCEPT', 'HTTP_ACCEPT_ENCODING']

    # 实际请求的请求头顺序
    request_headers = list(request.META.keys())
    print(list(request.META.keys()))

    # 判断实际请求的请求头【顺序】是否满足要求
    # 算法:如果实际请求头在要求里面，就截断要求头
    for standard_header in standard_headers:
        if standard_header in request_headers:
            request_headers = request_headers[request_headers.index(standard_header):]
            # print(request_headers)
        else:
            # return HttpResponse("failed")
            # return render(request, "section01/lesson3.html", {"my_name": "failed"})
            return JsonResponse({'result': 'failed'})
    # return HttpResponse("success")
    # return render(request, "section01/lesson3.html", {"my_name": "success"})
    return JsonResponse({'result': 'success'})


def lesson5_01(request):
    return render(request, "section01/lesson5.html")


def lesson5_data_api(request):
    print(request)
    token_list = request.GET.get("token").split("|")
    _sum = token_list[1]
    _time = token_list[0]
    _check_sum = 0
    for _number in _time:
        _check_sum += int(_number)
    if int(_sum) == _check_sum:
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return JsonResponse({"status": 200, "data": data}, status=200)
    else:
        return JsonResponse({"status": 200, "data": []}, status=403)


def lesson6_01(request):
    # return HttpResponse(request.environ.get("ssl_ciphers"))
    return render(request, "section01/lesson6.html")


def lesson6_data_api(request):
    token = request.GET.get("token")
    decode_result = int(''.join([chr(ord(i) - 1314) for i in token]))

    # 相差10s
    if abs(decode_result / 1000 - time.time()) <= 10 and len(request.environ.get("ssl_ciphers")) < 600:
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return JsonResponse({"status": 200, "data": data}, status=200)
    else:
        return JsonResponse({"status": 200, "data": []}, status=403)
