from django.conf.urls import patterns, include, url
from PsiU.views import landing_page, calendar, contact_us, phil, house, chapter, international,news,rush,scholar,movember
from brother_of_the_month.views import brother_of_the_month
from chapter_roll.views import chapter_roll
from django.conf.urls.static import static
from django.conf.urls.defaults import *
from django.conf import settings
from comments.views import contact, thanks
from email_spoofer.views import email
from instagram.views import instagram

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
#    url(r'^about/$',about),
    url(r'^calendar/$',calendar),
    url(r'^brother_of_the_month/$',brother_of_the_month),
    url(r'^rush/$',rush),
    url(r'^contact/$',contact),
    url(r'^chapter_roll/$',chapter_roll),

    url(r'^instagram/$',instagram),

    url(r'^thanks/$',thanks),


    url(r'^email_spoofer/$',email),

    url(r'^phil/$',phil),


    url(r'^house/$',house),
    url(r'^international/$',international),
    url(r'^chapter/$',chapter),

    url(r'^news/$',news),

    url(r'^scholar/$',scholar),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^movember/', movember),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
