from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'InvoiceCloud.views.home', name='home'),
                       # url(r'^InvoiceCloud/', include('InvoiceCloud.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'invoices.views.home', name='invoices_home'),
                       url(r'^login$', 'users.views.login', name='users_login'),
                       url(r'^logout$', 'users.views.logout', name='users_logout'),
                       url(r'^register$', 'users.views.register', name='users_register'),
                       url(r'^view_data', 'users.views.view_data', name='users_view_data'),
                       url(r'^ac/(?P<id>\d+)', 'users.views.activate_account', name='activate_account'),
                       url(r'^upload$', 'invoices.views.upload_new_efactura', name='upload_efactura'),
                       url(r'^download/(?P<id>\d+)', 'invoices.views.download_efactura', name='download_efactura'),
                       )
