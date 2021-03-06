from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

import main.views

# Examples:
# url(r'^$', 'spamtest.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^db', main.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^your-name/', main.views.get_name, name='get_name'),
]

handler404 = 'main.views.error404'