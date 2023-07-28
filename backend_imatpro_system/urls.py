"""backend_imatpro_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

app_name = 'imatpro/api/v1.0.0/mathematical/'

imatpro_patterns = ([
                        path('', include('com.sofyntelligen.imatpro.app.backend.architect.urls')),
                        path('', include('com.sofyntelligen.imatpro.app.backend.account.urls')),
                        path('', include('com.sofyntelligen.imatpro.app.backend.mathematical.catalog.urls')),
                        path('', include('com.sofyntelligen.imatpro.app.backend.mathematical.character.urls')),
                        path('', include('com.sofyntelligen.imatpro.app.backend.mathematical.equation.urls')),
                        path('', include('com.sofyntelligen.imatpro.app.backend.mathematical.representation.urls')),
                    ], 'imatpro')

urlpatterns = [
    path(app_name, include(imatpro_patterns)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
