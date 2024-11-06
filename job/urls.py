from django.urls import path , include
from . import views
from .views import jobDetail

urlpatterns = [

    path('' , views.jobList , name='job-list'),
    path('<int>:id', views.jobDetail , name='job-detail')
]