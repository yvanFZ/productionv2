from django.urls import path
from .views import CreateTestrapport,GetTestrapport,GetTestrapportOverzicht
app_name = 'testrapport'

urlpatterns = [
    path('create-testrapport',CreateTestrapport.as_view()),
    path('get-testrapportById',GetTestrapport.as_view()),
    path('get-testrapportoverzicht',GetTestrapportOverzicht.as_view())
]