from django.shortcuts import render
from . import models
from django.core.paginator import *
# # 进行分页练习
def herolist(request, pindex='1'):
    list = models.HeroInfo.objects.all()
    # 第一参数为所有内容 第二个参数为每页放几条
    paginator = Paginator(list, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'fenye1.html', context)


