from django.conf.urls import include, url
from . import views

urlpatterns = [


    #url(r'^myapp/$', HomeView.as_view(template_name='home.html'), name='home'),
    #url(r'^accounts/login/$', auth_views.login, {'watchout': 'login.html'}),
    #url(r'^$', 'django.contrib.auth.views.login', name='login'),

    url(r'^login/$', views.login, name='login'),
    url(r'^emp_home/$', views.emphome, name='emphome'),
    url(r'^timeleft/$', views.timeleft, name='timeleft'),
    url(r'^logusers/$', views.logusers, name='logusers'),  

#    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
]
