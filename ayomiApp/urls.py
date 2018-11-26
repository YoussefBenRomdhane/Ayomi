
from . import views
from django.conf.urls import url

urlpatterns = [
    url('index',views.index,name='index'),
    url('profil',views.profil,name='profil'),
    url('authentificate', views.authenticate_user, name='authentificate'),
    url('logout/', views.logout_view, name='logout'),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    url(r'^submit_edition_user/(?P<p_id>[0-9]+)$', views.submit_edition_user, name='submit_edition_user'),

]


