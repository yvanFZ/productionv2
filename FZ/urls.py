from django.urls import path,include, re_path
from django.views.generic import TemplateView


# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('project/', include('project.urls')),
    path('mpo/', include('mpo.urls')),
    path('testrapport/', include('testrapport.urls')),
    path('opleverrapport/', include('opleverrapport.urls')),
    path('productiestatusicem/', include('productiestatusicem.urls')),
    

]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name = 'index.html'))] # voor react