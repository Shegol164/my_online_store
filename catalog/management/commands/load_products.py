from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Загружает продукты из фикстур'

    def handle(self, *args, **options):
        # Очистка старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        electronics = Category.objects.create(
            name="Электроника",
            description="Техника и гаджеты"
        )

        books = Category.objects.create(
            name="Книги",
            description="Художественная литература"
        )

        # Создание продуктов
        Product.objects.create(
            name="Смартфон",
            description="Флагманский телефон",
            category=electronics,
            price=799.99
        )

        Product.objects.create(
            name="Ноутбук",
            description="Игровой ноутбук",
            category=electronics,
            price=1499.99
        )

        Product.objects.create(
            name="Роман",
            description="Бестселлер",
            category=books,
            price=19.99
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Создано: {Category.objects.count()} категорий, "
                f"{Product.objects.count()} продуктов"
            )
        )