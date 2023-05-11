from django.urls import path
from .views import GetDataToPrint,Getproductiebon,UpdateMPO,GetMPO,CreateProductieStatus,GetProductieStatus,GetAllSiteByProject

app_name = 'mpo'

urlpatterns = [
    path('update-mpo',UpdateMPO.as_view(),name='update'),
    path('get-mpo',GetMPO.as_view()),
    path('create-productiestatus',CreateProductieStatus.as_view()),
    path('get-productiestatus',GetProductieStatus.as_view()),
    path('get-sitesProject',GetAllSiteByProject.as_view()),
    path('get-productiebon',Getproductiebon.as_view()),
    path('get-datatoprint',GetDataToPrint.as_view()),


]