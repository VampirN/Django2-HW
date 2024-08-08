from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        max_length=1000, verbose_name="описание", help_text="Введите описание категории",
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        max_length=1000, verbose_name="описание", help_text="Введите описание продукта",
    )
    img_preview = models.ImageField(
        upload_to="imgproduct/",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        help_text="Введите категорию товара",
        related_name="products",
    )
    price = models.PositiveIntegerField(
        verbose_name="цена за покупку", help_text="Введите цену продукта"
    )
    created_at = models.DateTimeField(
        verbose_name="дата создания", default=timezone.now
    )
    last_modified_date = models.DateTimeField(
        verbose_name="дата последнего изменения", default=timezone.now
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = (
            "name",
            "category",
        )



