# app/serializers.py

from rest_framework import serializers
from .models import Dictionary, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'original_word', 'translated_word', 'image', 'dictionary']


class DictionarySerializer(serializers.ModelSerializer):
    # Показываем имя владельца, но делаем поле доступным только для чтения.
    # Пользователь не должен иметь возможности назначать владельца вручную.
    owner = serializers.ReadOnlyField(source='owner.username')
    # Включаем вложенный список слов для каждого словаря
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Dictionary
        # Включаем новое поле owner и вложенные words в ответ API
        fields = ['id', 'name', 'created_at', 'owner', 'words']