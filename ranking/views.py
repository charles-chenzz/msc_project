from django.shortcuts import render
from index.models import *
from django.views.generic import ListView


# Create your views here.

def rankingView(request):
    # 搜索歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    # 歌曲分类列表
    labels = Label.objects.all()
    # 歌曲列表信息
    t = request.GET.get('type', '')
    if t:
        dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
    else:
        dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
    return render(request, 'ranking.html', locals())


class RankingList(ListView):
    # context_object_name 设置html模板的某一个变量名称
    context_object_name = 'dynamics'
    # 设定模板文件
    template_name = 'ranking.html'

    # 设置dynamics的数据
    def get_queryset(self):
        # 获取请求参数
        t = self.request.GET.get('type', '')
        if t:
            dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
        else:
            dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
        return dynamics

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        # 搜索歌曲
        context['searchs'] = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
        # 所有歌曲分类
        context['labels'] = Label.objects.all()
        return context
