from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.urlresolvers import reverse
# Create your views here.
#首页
def index(request):
    list = Article.objects.all().values()
    content = {'list':list}
    return render(request,'myblog/index.html',content)

#详情
def detail(request,id):
    article = Article.objects.get(pk=id)
    content = {'article':article}
    return render(request,'myblog/detail.html',content)

#编辑
def editpage(request):
    return render(request,'myblog/editpage.html')

#编辑页面
def editpage_handle(request):
    title = request.POST.get('title','')
    print(title)
    content = request.POST.get('content','')
    #存储到数据库
    a = Article()
    a.atitle = title
    a.acontent = content
    a.aread = 0
    a.save()
    # return redirect('/blog/index')
    return redirect(reverse('blog:index'))


def inde(request,id):
    # return HttpResponse('index')
    a = Article.objects.get(pk=id)
    a.isDelete = False
    a.save()
    list=Article.objects.filter(isDelete=True)
    return render(request,'myblog/index.html',{'list':list})
