from django.urls import path, include, re_path
# from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()

import site_content.views
import cms.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
	re_path(r'^jet/', include(('jet.urls', 'jet'))),
	re_path(r'^jet/dashboard/', include(('jet.dashboard.urls', 'jet-dashboard'))), 
#  	path("", site_content.views.home_page),
#  	path("mobile/", site_content.views.mobile_landing),
#  	path("", site_content.views.home_page),
  	path("", cms.views.home_page),
 	path("mobile/", cms.views.mobile_landing),
	path("admin/", admin.site.urls),
	path("api/", cms.views.api),
	path("public_api/", cms.views.public_api),
#  	path("<page>/", site_content.views.dynamic_page),
	path("<page>/", cms.views.dynamic_page),
#	path("<auth>/<page>", cms.views.dynamic_page),
#	path("members/<page>", cms.views.members),
#	path("members/<page>", cms.views.members),
#	path("members/<page>", cms.views.members),
	path("summernote/", include("django_summernote.urls")),
# #    path("", hello.views.index, name="index"),
# #    path("db/", hello.views.db, name="db"),
# # 	path("blog/", site_content.views.blog_home),
# # 	path("blog/<page>", site_content.views.blog),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
# 	url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
# 	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
# 	url(r'^admin/', include(admin.site.urls)),
# ]

admin.site.site_header = 'Null Horizon'
