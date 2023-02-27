from django.urls import path
from .views import GetOpleverrapportOverzicht,GetOpleverrapport,CreateOpleverRapport
app_name = 'opleverrapport'

urlpatterns = [
    path('create-opleverrapport',CreateOpleverRapport.as_view()),
    path('get-opleverrapportById',GetOpleverrapport.as_view()),
    path('get-opleverrapportoverzicht',GetOpleverrapportOverzicht.as_view())
]