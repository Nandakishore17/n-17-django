
from django.urls import path,include
from . import views

urlpatterns = [
path('test',views.TestFun,name='test'),

path('test1',views.TestFun1,name='test1'),
path('test2',views.TestFun2,name='test2'),
path('test3',views.TestFun3,name='test3'),
path('test4',views.TestFun4,name='test4'),
]
