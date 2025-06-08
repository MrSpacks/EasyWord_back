# app/admin.py

from django.contrib import admin
from .models import Dictionary, Word

@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('original_word', 'translated_word', 'dictionary')
    list_filter = ('dictionary__owner', 'dictionary')
    search_fields = ('original_word', 'translated_word')