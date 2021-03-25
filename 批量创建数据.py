import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app01.models import User

    user_list = (User(name='用户{}'.format(i)) for i in range(100))
    User.objects.bulk_create(user_list)
