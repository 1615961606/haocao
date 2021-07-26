from django.conf.urls import include,url
from . import views

urlpatterns = [
    #首页
    url(r'^index/$',views.index,name='index'),
    #详情
    url(r'^detail/(\d+)$', views.detail,name='detail'),
    #编辑
    url(r'^editpage/$',views.editpage,name='editpage' ),
    #编辑提交
    url(r'^editpagehandle/$',views.editpage_handle,name='editpagehandle' ),

    url(r'^delete/(?P<id>[0-9]+)',views.inde,name='delete'),
]