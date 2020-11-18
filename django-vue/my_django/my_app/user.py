from rest_framework.views import APIView
from rest_framework.response import Response

# 导入sqlite3
from .models import *

# 导入核心代码
from .user_utils import draw_code_img,make_password

# 导入随机库
import random


# 获取验证码
class GetCode(APIView):
    def get(self, request):
        # 验证码内容
        img = draw_code_img()
        return Response(img)


# 注册
class Register(APIView):
    def get(self, request):
        # 注册进行步骤 0 验证手机号  1 设置账号密码
        type = request.GET.get("type")
        # 手机号
        phone = request.GET.get("phone")
        if type == "0":
            # 手机验证码
            yzm = request.GET.get("yzm")
            # 用户输入的验证码
            user_yzm = request.GET.get("user_yzm")
            if yzm != user_yzm:
                return Response({"code": "1"})
            # 验证手机号是否存在
            if phone:
                return Response({"code": "1", "msg": "已注册"})
            return Response({"code": "0", "msg": "注册成功"})
        if type == "1":
            # 电子邮箱
            e_mail = request.GET.get("e_mail")
            s = str(random.randint(0, 99999999)).zfill(10)
            # 用户名称
            username = (
                request.GET.get("username")
                if request.GET.get("username")
                else f"用户{s}"
            )
            # 密码
            password = request.GET.get("password")
            # 加密
            password = make_password(password)
            User(username=username,password=password,phone=phone,e_mail=e_mail)
            return Response({"code": "0", "msg": "注册成功"})