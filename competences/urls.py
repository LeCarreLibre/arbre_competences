from django.conf.urls import url
from competences.views import ListeProfils, AffichageProfil

urlpatterns = [
    url(r'^$', ListeProfils.as_view()),
    url(r'^profils/$', ListeProfils.as_view(), name="liste_profils"),
    url(r'^profil/(?P<pk>\d+)', AffichageProfil.as_view(),
        name="affichage_profil"),
]
