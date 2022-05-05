from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maker.urls'))
]

handler404 = 'maker.views.not_found_404'
handler500 = 'maker.views.server_error_500'
