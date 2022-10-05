from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    # path('routine/', include('apps.routine.urls')),
    path('manager/', admin.site.urls),
]
admin.site.site_header = 'Gestão Next Aid'
admin.site.site_title = 'Gestão Next Aid'
admin.site.index_title = 'Área Administrativa'
