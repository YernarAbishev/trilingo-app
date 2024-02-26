from django.db import models
from pytils.translit import slugify

class EnglishAlphabet(models.Model):
    name = models.CharField("Буква", max_length=10)
    image = models.ImageField("Изображение", upload_to="alphabet/en/", default="")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Англйиский алфавит"
        verbose_name_plural = "Английский алфавит"

class RussianAlphabet(models.Model):
    name = models.CharField("Буква", max_length=10)
    image = models.ImageField("Изображение", upload_to="alphabet/ru/", default="")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Русский алфавит"
        verbose_name_plural = "Русский алфавит"

class KazakhAlphabet(models.Model):
    name = models.CharField("Буква", max_length=10)
    image = models.ImageField("Изображение", upload_to="alphabet/kz/", default="")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Казахский алфавит"
        verbose_name_plural = "Казахский алфавит"

class WorkingClass(models.Model):
    name = models.CharField("Название класса", max_length=35)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

class Theme(models.Model):
    working_class = models.ForeignKey(WorkingClass, on_delete=models.CASCADE, verbose_name="Выберите класс", default="")
    word_kz = models.CharField("Название темы на казахском", max_length=35, default="")
    word_ru = models.CharField("Название темы на русском", max_length=35, default="")
    word_en = models.CharField("Название темы на английском", max_length=35, default="")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.word_kz} - {self.word_ru} - {self.word_en}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.word_kz)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

class WordInKz(models.Model):
    alphabet = models.ForeignKey(KazakhAlphabet, on_delete=models.CASCADE, verbose_name="Буква на казахском")
    word = models.CharField("Название слова", max_length=90)
    subword = models.CharField("Дополнительно", max_length=160)
    description = models.TextField("Описание")
    voice = models.FileField("Произношение", upload_to="voices/kz/")

    def __str__(self):
        return f"{self.word}"

    class Meta:
        verbose_name = "Слово на казахском"
        verbose_name_plural = "Слова на казахском"

class WordInRu(models.Model):
    alphabet = models.ForeignKey(RussianAlphabet, on_delete=models.CASCADE, verbose_name="Буква на русском")
    word = models.CharField("Название слова", max_length=90)
    subword = models.CharField("Дополнительно", max_length=160)
    description = models.TextField("Описание")
    voice = models.FileField("Произношение", upload_to="voices/ru/")

    def __str__(self):
        return f"{self.word}"

    class Meta:
        verbose_name = "Слово на русском"
        verbose_name_plural = "Слова на русском"

class WordInEn(models.Model):
    alphabet = models.ForeignKey(EnglishAlphabet, on_delete=models.CASCADE, verbose_name="Буква на английском")
    word = models.CharField("Название слова", max_length=90)
    transcript = models.CharField("Транскрипт (необязательное поле)", max_length=160, null=True, blank=True)
    subword = models.CharField("Дополнительно", max_length=160)
    description = models.TextField("Описание")
    voice = models.FileField("Произношение", upload_to="voices/en/")

    def __str__(self):
        return f"{self.word}"

    class Meta:
        verbose_name = "Слово на английском"
        verbose_name_plural = "Слова на английском"

class Words(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name="Тема")
    word_kz = models.ForeignKey(WordInKz, on_delete=models.CASCADE, verbose_name="Слово на казахском")
    word_ru = models.ForeignKey(WordInRu, on_delete=models.CASCADE, verbose_name="Слово на русском")
    word_en = models.ForeignKey(WordInEn, on_delete=models.CASCADE, verbose_name="Слово на английском")
    image = models.ImageField("Изображение", upload_to="words/")

    def __str__(self):
        return f"{self.pk}"


    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"







