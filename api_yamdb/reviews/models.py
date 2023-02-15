from datetime import datetime


from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


# создать приложение ТИТЛс с файлами админ, приложение, модели
class Category(models.Model):
    """Модель для категорий."""

    name = models.CharField(
        "Наименование категории", max_length=150
    )  # max_length-?
    slug = models.SlugField("Путь категории", unique=True)

    class Meta:
        ordering = ("slug",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug


class Genre(models.Model):
    """Модель для жанров."""

    name = models.CharField(
        "Наименование жанра", max_length=150
    )  # max_length-?
    slug = models.SlugField("Путь жанра", unique=True)

    class Meta:
        ordering = ("slug",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.slug


class Title(models.Model):
    """Модель для произведений."""

    name = models.CharField(
        "Наименование произведения", max_length=150
    )  # max_length-?
    year = models.IntegerField(
        "Год выпуска", validators=[MaxValueValidator(int(datetime.now().year))]
    )
    description = models.TextField(
        "Описание",
    )
    # rating?
    genre = models.ManyToManyField(
        Genre,
        # through='GenreTitle',
        blank=True,
        related_name="titles",
        verbose_name="Жанр",
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name="titles",
        verbose_name="Категория",
    )

    class Meta:
        ordering = ("year",)
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre_id = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name="genres",
        verbose_name="Жанры",
    )
    title_id = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        null=True,
        related_name="titles",
        verbose_name="Произведения",
    )


class Review(models.Model):
    """Модель для Отзыва+рейтинг."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name="Произведение"
    )
    text = models.TextField("Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        verbose_name="Оценка",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для Комментария к Отзыву."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField("Текст комментария")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.text
