"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from polls import views

app_name = 'polls'

urlpatterns = [

    url(r'^polls/$', views.index, name='index'),
    url(r'^polls/(?P<question_id>[0-9])/$', views.detail, name='detail'),
    # url('polls/<int:question_id>/', views.detail, name='detail'),
    url(r'^polls/<int:question_id>/results/', views.results, name='results'),
    url(r'^polls/(?P<question_id>[0-9])/vote/$', views.vote, name='vote'),
    # url(r'^polls/<int:question_id>/vote/', views.vote, name='vote'),
]
