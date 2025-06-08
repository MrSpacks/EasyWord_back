# app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# ↓↓↓ Убедитесь, что импорт идет из .views (из текущей папки) ↓↓↓
from .views import DictionaryViewSet, WordViewSet

router = DefaultRouter()
# ↓↓↓ Здесь мы используем названия 'dictionaries' и 'words' для конечных точек API ↓↓↓
router.register(r'dictionaries', DictionaryViewSet, basename='dictionary')
router.register(r'words', WordViewSet, basename='word')

urlpatterns = [
    path('', include(router.urls)),
]