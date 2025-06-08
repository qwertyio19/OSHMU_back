from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.yasg import urlpatterns_yasg

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urlpatterns_yasg))
]

urlpatterns += i18n_patterns(
    path("api/v1/users/", include("apps.users.urls")),
    # path("api/v1/fkj/", include("apps.FKJ.urls")),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)