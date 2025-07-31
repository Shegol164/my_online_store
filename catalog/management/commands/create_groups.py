from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Creates moderator group with permissions'

    def handle(self, *args, **options):
        # Создаем группу модераторов
        mod_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Добавляем права
        content_type = ContentType.objects.get_for_model(Product)

        permissions = [
            'can_unpublish_product',
            'can_change_product_status',
            'delete_product',  # стандартное право на удаление
        ]

        for perm in permissions:
            try:
                permission = Permission.objects.get(
                    codename=perm,
                    content_type=content_type
                )
                mod_group.permissions.add(permission)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Permission {perm} not found'))

        self.stdout.write(self.style.SUCCESS('Successfully created moderator group'))