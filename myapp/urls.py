
from django.urls import path,include
from . import views

urlpatterns = [
path('test',views.TestFun,name='test'),

path('test1',views.TestFun1,name='test1'),

]
