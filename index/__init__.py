from django.apps import AppConfig
import os

# 修改app在admin后台显示名称
# default_app_config的值来自己app.py的类名
default_app_config = 'index.IndexConfig'

# 获取当前app的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

# 重写类IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'
