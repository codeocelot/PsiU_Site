from django.conf.urls import patterns, include, url
from PsiU.views import landing_page, about, calendar, rush, contact_us
from brother_of_the_month.views import brother_of_the_month
from chapter_roll.views import chapter_roll
from django.conf.urls.static import static
from django.conf import settings

from email_spoofer.views import email

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
    url(r'^rush/$',rush),
    url(r'^contact_us/$',contact_us),
    url(r'^chapter_roll/$',chapter_roll),

    url(r'^email_spoofer$',email),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
