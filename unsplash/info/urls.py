from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^tag/(\d+)',views.tags_page,name='tag_view'),
    url(r'^search/',views.search_results,name="search_results"),
    url(r'^new/',views.new_photos,name="new"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)