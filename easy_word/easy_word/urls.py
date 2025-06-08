# easy_word/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Импортируем представления для получения токенов
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # ↓↓↓ Самое главное: подключаем URL-адреса из вашего приложения "app" ↓↓↓
    path('app/', include('app.urls')),

    # Эндпоинты для аутентификации по токенам
    path('app/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('app/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Это нужно для того, чтобы Django мог отдавать медиафайлы в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)