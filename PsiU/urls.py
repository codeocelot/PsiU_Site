from django.conf.urls import patterns, include, url
from PsiU.views import landing_page, about, calendar, rush
from brother_of_the_month.views import brother_of_the_month
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PsiU.views.home', name='home'),
    # url(r'^PsiU/', include('PsiU.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',landing_page),
    url(r'^about/$',about),
    url(r'^calendar/$',calendar),
    url(r'^brother_of_the_month/$',brother_of_the_month),
    url(r'^rush/$',rush)
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
