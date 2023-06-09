from django.urls import path
from .views import BewerkenKlantMedeweker,GetProjectDataVoorBewerken,UpdateProject,GetAllProjects,GetProjectById,GetProjectItems,CreateProjectView,CreateKlantMedewerkerView,CreateKlant,AllProjectsList,CreateOnderaanemer,ListOnderaanemer

app_name = 'project'

urlpatterns = [
    path('get-project',GetProjectItems.as_view()),
    path('post-project',CreateProjectView.as_view()),
    path('post-klantMedewerker',CreateKlantMedewerkerView.as_view()),
    path('post-klant',CreateKlant.as_view()),
    # path(r'^getProjectID/(?P<id>\d+)/$',GetProjectById.as_view()),
    path('getProjectID',GetProjectById.as_view()),
    path('getProjectBewerken',GetProjectDataVoorBewerken.as_view()),
    path('get-all-projects',GetAllProjects.as_view()),
    path('update-project',UpdateProject.as_view()),
    path("getallproject",AllProjectsList.as_view()),
    path("post-bedrijfsaanemer",CreateOnderaanemer.as_view()),
    path("get-bedrijfsaanemer",ListOnderaanemer.as_view()),
    path('edit-klantMedewerker',BewerkenKlantMedeweker.as_view())
    # re_path('list/',login_required(LeadListView.as_view()),name="list-leads"),
    # re_path('',login_required(CreateVertegenwoordigersLead.as_view()),name="create-vertegenwoordiger")
    ]