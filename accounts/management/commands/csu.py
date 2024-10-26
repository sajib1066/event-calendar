from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            user_class = get_user_model()
            user = user_class.objects.create(
                email='admin@admin.ru',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )

            user.set_password('admin')
            user.save()

        except Exception as e:
            return f"Ошибка создания супер пользователя, он уже создан {e}"
