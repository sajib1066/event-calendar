from django.core.management import BaseCommand

from ...models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.create(
                email='vlad',
                is_staff=True,
                is_superuser=True,
                is_active=True
            )

            user.set_password('1')
            user.save()

        except Exception as e:
            return f"Ошибка создания супер пользователя, он уже создан {e}"
