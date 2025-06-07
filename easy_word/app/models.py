# api/models.py

from django.db import models
from django.contrib.auth.models import User # <-- Импортируем модель User

class Dictionary(models.Model):
    # ↓↓↓ Добавляем это поле ↓↓↓
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dictionaries', verbose_name="Владелец")
    name = models.CharField(max_length=100, verbose_name="Название словаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Словарь"
        verbose_name_plural = "Словари"
        # Добавим ограничение, чтобы у одного пользователя не было словарей с одинаковым названием
        unique_together = ('owner', 'name')


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='words', verbose_name="Словарь")
    original_word = models.CharField(max_length=255, verbose_name="Оригинальное слово")
    translated_word = models.CharField(max_length=255, verbose_name="Перевод")
    image = models.ImageField(upload_to='word_images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.original_word} - {self.translated_word}"

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['-created_at']