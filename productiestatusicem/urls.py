from django.urls import path
from .views import GetProductiestatusIcemOverzicht,AanmakenProductieStatusIcem

app_name = 'productiestatusicem'

urlpatterns = [
    path('get-productiestatusicem',GetProductiestatusIcemOverzicht.as_view()),
    path('create-productiestatusicem',AanmakenProductieStatusIcem.as_view())
]