from django.shortcuts import render

# app/views.py

from rest_framework import viewsets, permissions
from .models import Dictionary, Word
from .serializers import DictionarySerializer, WordSerializer

class DictionaryViewSet(viewsets.ModelViewSet):
    """
    RU: API эндпоинт для просмотра и редактирования словарей.
    CZ: API endpoint pro zobrazení a editování slovníků.
    """
    serializer_class = DictionarySerializer # serializer
    permission_classes = [permissions.IsAuthenticated] # permission

    def get_queryset(self):
        """
        RU: Этот view должен возвращать список словарей
        только для текущего аутентифицированного пользователя.
        CZ: Tento view musí vracet seznam slovníků
        pouze pro aktuálního autentifikovaného uzivatele.
        """ 
        return self.request.user.dictionaries.all() 

    def perform_create(self, serializer):
        """
        RU: При создании нового словаря, назначаем его владельцем
        текущего пользователя.
        CZ: Prí pridání noveho slovnika, priradime ho vlastnikovi
        aktuálního uzivatele.
        """
        serializer.save(owner=self.request.user)


class WordViewSet(viewsets.ModelViewSet):
    """
    RU: API эндпоинт для слов.
    CZ: API endpoint pro slova.
    """
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        RU:Возвращаем слова только из словарей,
        принадлежащих текущему пользователю.
        CZ: Vracíme slova pouze z slovníků,
        které patria aktuálnímu uzivateli.
        """
        return Word.objects.filter(dictionary__owner=self.request.user)