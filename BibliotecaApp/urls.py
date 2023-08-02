from django.contrib import admin
from django.urls import path, include
from rest_framework import documentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("WebBiblio.urls")),
    path('api/', include("api.urls")),
    path("api-rest/",
         documentation.include_docs_urls(title="API Biblioteca", description="Documentacion de la API Biblioteca",
                                         public=True)),
]
