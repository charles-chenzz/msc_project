import datetime

from django.db import models


# Create your models here.
class Label(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('分类标签', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        # 设置admin界面的显示内容
        verbose_name = '歌曲分类'
        verbose_name_plural = '歌曲分类'


class Song(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('歌名', max_length=50)
    singer = models.CharField('歌手', max_length=50)
    time = models.CharField('时长', max_length=10)
    album = models.CharField('专辑', max_length=50)
    languages = models.CharField('语种', max_length=20)
    type = models.CharField('类型', max_length=20)
    release = models.DateField('发行时间', default=datetime.date.today)
    img = models.FileField("歌曲图片", upload_to='songImg/', default='暂无图片')
    lyrics = models.FileField('歌词', upload_to='songLyric/', default='暂无歌词', blank=True)
    file = models.FileField('歌曲文件', upload_to='songFile/', default='暂无文件')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name='歌名分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'

class Dynamic(models.Model):
    id = models.AutoField('序号', primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    plays = models.IntegerField('播放次数', default=0)
    search = models.IntegerField('搜索次数', default=0)
    download = models.IntegerField('下载次数', default=0)

    class Meta:
        verbose_name = '歌曲动态'
        verbose_name_plural = '歌曲动态'


class Comment(models.Model):
    id = models.AutoField('序号', primary_key=True)
    text = models.CharField('内容', max_length=500)
    user = models.CharField('用户', max_length=20)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    date = models.DateField('日期', auto_now=True)

    class Meta:
        verbose_name = '歌曲评论'
        verbose_name_plural = '歌曲评论'
