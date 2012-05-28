# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = patterns('',  
        
    url(r'^register/user/?$', 'Shaastra-2013-Website.users.views.user_registration'),
#      (r'^edit/user/?$', 'Shaastra-2013-Website.users.views.edit_profile'),
#      (r'^register/college/?$', 'Shaastra-2013-Website.users.views.college_registration'),
#      (r'^register/activate/(?P<a_key>[\w]+)/?$', 'Shaastra-2013-Website.users.views.activate'),
    url(r'^login/?$', 'Shaastra-2013-Website.users.views.login'),
    url(r'^logout/?$', 'Shaastra-2013-Website.users.views.logout'),
    url(r'^facebook/login/?$', 'Shaastra-2013-Website.users.fb_views.login'),
    url(r'^facebook/authentication_callback/?$', 'Shaastra-2013-Website.users.fb_views.authentication_callback'),
#      (r'^feedback/?$', 'Shaastra-2013-Website.users.views.feedback'),
#      (r'^view_feedback/?$', 'Shaastra-2013-Website.users.views.view_feedback'),
#      (r'^password_change/$', 'django.contrib.auth.views.password_change'),
#      (r'^password_change/done/$', 'django.contrib.auth.views.password_change_done'),
#      (r'^myshaastra/forgot_password/$', 'Shaastra-2013-Website.users.views.forgot_password'),
#      (r'^myshaastra/forgot_password/done/$', direct_to_template, { 'template' : 'users/forgot_password_done.html', } ),
#      (r'^myshaastra/reset_password/$', 'Shaastra-2013-Website.users.views.reset_password'),
#      (r'^myshaastra/reset_password/done/$', direct_to_template, { 'template' : 'users/reset_password_done.html', } ),
#      (r'^myshaastra/edit_profile/$','Shaastra-2013-Website.users.views.edit_profile'),
#      (r'^spons/$', 'Shaastra-2013-Website.users.views.spons_dashboard'),
#    url(r'^logout$', 'django.contrib.auth.views.logout'),


)   


