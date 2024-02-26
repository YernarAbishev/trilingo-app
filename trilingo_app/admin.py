from django.contrib import admin
from .models import WorkingClass, Theme, EnglishAlphabet, RussianAlphabet, KazakhAlphabet, WordInEn, WordInKz, WordInRu, Words

admin.site.register(WorkingClass)
admin.site.register(Theme)
admin.site.register(KazakhAlphabet)
admin.site.register(EnglishAlphabet)
admin.site.register(RussianAlphabet)
admin.site.register(WordInKz)
admin.site.register(WordInRu)
admin.site.register(WordInEn)
admin.site.register(Words)