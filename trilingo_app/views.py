from django.shortcuts import render, get_object_or_404
from .models import WorkingClass, Theme, EnglishAlphabet, RussianAlphabet, KazakhAlphabet, WordInEn, WordInKz, WordInRu, Words
from django.db.models import Q


def home_page(request):
    working_classes = WorkingClass.objects.all()
    context = {
        'working_classes': working_classes
    }
    return render(request, "./home.html", context)

def themes_page(request, slug):
    working_class = get_object_or_404(WorkingClass, slug=slug)
    themes = Theme.objects.filter(working_class=working_class)
    context = {
        'working_class': working_class,
        'themes': themes
    }
    return render(request, "./themes.html", context)

def theme_detail_page(request, slug):
    theme = get_object_or_404(Theme, slug=slug)
    words = Words.objects.filter(theme=theme)
    context = {
        'theme': theme,
        'words': words
    }
    return render(request, "./theme-detail.html", context)

def alphabets_kz_page(request):
    alphabets = KazakhAlphabet.objects.all()
    context = {
        'alphabets': alphabets
    }
    return render(request, "./alphabets_kz.html", context)

def alphabets_ru_page(request):
    alphabets = RussianAlphabet.objects.all()
    context = {
        'alphabets': alphabets
    }
    return render(request, "./alphabets_ru.html", context)

def alphabets_en_page(request):
    alphabets = EnglishAlphabet.objects.all()
    context = {
        'alphabets': alphabets
    }
    return render(request, "./alphabets_en.html", context)




def filter_by_kz_page(request, slug):
    alphabet = get_object_or_404(KazakhAlphabet, slug=slug)
    words = WordInKz.objects.filter(alphabet=alphabet)
    context = {
        'alphabet': alphabet,
        'words': words
    }
    return render(request, "./words-by-kz.html", context)

def filter_by_ru_page(request, slug):
    alphabet = get_object_or_404(RussianAlphabet, slug=slug)
    words = WordInRu.objects.filter(alphabet=alphabet)
    context = {
        'alphabet': alphabet,
        'words': words
    }
    return render(request, "./words-by-ru.html", context)

def filter_by_en_page(request, slug):
    alphabet = get_object_or_404(EnglishAlphabet, slug=slug)
    words = WordInEn.objects.filter(alphabet=alphabet)
    context = {
        'alphabet': alphabet,
        'words': words
    }
    return render(request, "./words-by-en.html", context)