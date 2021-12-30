from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from index.models import *


# Create your views here.

def searchView(request, page):
    if request.method == 'GET':
        # 热搜歌曲
        searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
        # 获取搜索内容 如果kword为空即查全部歌曲
        kword = request.session.get('kword', '')
        if kword:
            # Q是sql里的or语法
            song_info = Song.objects.values('id', 'name', 'singer', 'time').filter(
                Q(name__icontains=kword) | Q(singer=kword)).order_by('-release').all()
        else:
            song_info = Song.objects.values('id', 'name', 'singer', 'time').order_by(
                '-release').all()[:50]
        # 分页功能
        paginator = Paginator(song_info, 5)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        # 添加歌曲搜索次数
        song_exist = Song.objects.filter(name=kword)
        if song_exist:
            song_id = song_exist[0].song_id
            # 判断歌曲动态信息是否存在 存在则在原来基础加1
            dynamics = Dynamic.objects.filter(song_id=int(id)).first()
            if dynamics:
                dynamics.search += 1
                dynamics.save()
            else:
                dynamic = Dynamic(plays=0, search=1, download=0, song_id=id)
                dynamic.save()
        return render(request, 'search.html', locals())
    else:
        request.session['kword'] = request.POST.get('kword', '')
        return redirect('/search/1.html')
