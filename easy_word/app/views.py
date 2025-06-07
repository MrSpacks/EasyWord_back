from django.shortcuts import render

# api/views.py

from rest_framework import viewsets, permissions
from .models import Dictionary, Word
from .serializers import DictionarySerializer, WordSerializer

class DictionaryViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для просмотра и редактирования словарей.
    """
    serializer_class = DictionarySerializer
    # ↓↓↓ Только аутентифицированные пользователи могут получить доступ ↓↓↓
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Этот view должен возвращать список словарей
        только для текущего аутентифицированного пользователя.
        """
        return self.request.user.dictionaries.all()

    def perform_create(self, serializer):
        """
        При создании нового словаря, назначаем его владельцем
        текущего пользователя.
        """
        serializer.save(owner=self.request.user)


class WordViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для слов.
    """
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Возвращаем слова только из словарей,
        принадлежащих текущему пользователю.
        """
        return Word.objects.filter(dictionary__owner=self.request.user)