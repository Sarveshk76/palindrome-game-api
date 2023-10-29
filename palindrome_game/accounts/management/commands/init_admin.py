from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    username='admin'
    password='admin'

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            user = User.objects.create_user(self.username, password=self.password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            
            print(f'Admin account created (username: {self.username}, password: {self.password}).)')
        else:
            print('Admin account already exists.')