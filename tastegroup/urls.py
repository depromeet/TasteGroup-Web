from django.conf.urls import url
from . import views     # 이 파일의 현재 디렉토리인 blog 디렉토리의 뷰 사용

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^detail$', views.detail, name='detail'),
    
]
