from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .models import Dictionary, Word      

class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')  # Поиск по имени словаря и имени владельца
    list_filter = ('owner', 'created_at')  # Фильтрация по владельцу и дате создания

class WordAdmin(admin.ModelAdmin):
    list_display = ('original_word', 'translated_word', 'dictionary', 'created_at')
    search_fields = ('original_word', 'translated_word', 'dictionary__name')  # Поиск по оригинальному слову, переводу и названию словаря
    list_filter = ('dictionary', 'created_at')  # Фильтрация по словарю и дате создания

admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Word, WordAdmin)