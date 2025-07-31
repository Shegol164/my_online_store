from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    objects = None
    PUBLISH_STATUS = [
        ('published', 'Опубликован'),
        ('moderation', 'На модерации'),
        ('rejected', 'Отклонен'),
    ]

    status = models.CharField(
        max_length=20,
        choices=PUBLISH_STATUS,
        default='moderation',
        verbose_name='Статус публикации'
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    status = models.CharField(
        max_length=20,
        choices=PUBLISH_STATUS,
        default='moderation',
        verbose_name='Статус'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Владелец'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
            ("can_change_product_status", "Может менять статус продукта"),
        ]

    def __str__(self):
        return self.name