from django.urls import path
from .views import CreateMPO,GetMPO,CreateProductieStatus,GetProductieStatus,GetAllSiteByProject

app_name = 'mpo'

urlpatterns = [
    path('create-mpo',CreateMPO.as_view()),
    path('get-mpo',GetMPO.as_view()),
    path('create-productiestatus',CreateProductieStatus.as_view()),
    path('get-productiestatus',GetProductieStatus.as_view()),
    path('get-sitesProject',GetAllSiteByProject.as_view())
]