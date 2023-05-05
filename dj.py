from django.conf import settings
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('allauth.urls'))

]
if settings.DEBUG:
    importdebug_toolbar
    urlpatterns +=[path('_debug_/', include(debug_toolbar.urls))]