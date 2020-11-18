import datetime
import uuid

from django.db import models

# Create your models here.

class Base(models.Model):
    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.now(), null=True)

    class Meta:
        abstract = True

# 用户信息表
class User(Base):
    # 主键
    id = models.IntegerField(primary_key=True,default=uuid.uuid4(),max_length=36)
    # 用户名
    username = models.CharField(max_length=100)
    # 登录账号
    login_name = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=200)
    # 手机号
    phone = models.CharField(max_length=11)
    # 电子邮箱
    e_mail = models.CharField(max_length=50)

    class Meta:
        db_table = "user"
