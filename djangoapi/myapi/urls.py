
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('myapi',views.ApprovalsView)

urlpatterns = [
    path('form/',views.myform,name='myform'),
    path('api/',include(router.urls)),
    path('status/',views.approvereject)


]
