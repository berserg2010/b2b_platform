from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('b2b-auth/', include('b2b_auth.urls')),

    path('', include('public_side.urls')),

    path('private_side/', include('private_side.urls')),
]
