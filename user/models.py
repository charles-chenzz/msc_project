from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):
    qq = models.CharField('QQ号', max_length=20)
    weChat = models.CharField('微信号', max_length=20)
    mobile = models.CharField('手机号', max_length=11, unique=True)

    # 设置返回值
    def __str__(self):
        return self.username
