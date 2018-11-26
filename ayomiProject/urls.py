

from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    # url(r'^$', 'ayomiProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('admin/',  admin.site.urls),
    url('Ayomi/', include('ayomiApp.urls'))
]
