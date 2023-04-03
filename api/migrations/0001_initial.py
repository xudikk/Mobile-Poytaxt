#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Phone')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('is_sms', models.BooleanField(default=False)),
                ('is_test', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('identity', models.CharField(default='TT', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '1. Users',
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Error code')),
                ('alias', models.IntegerField(null=True, verbose_name='Alias Code from origin')),
                ('origin', models.CharField(default='Poytaxt Mobile', max_length=50, verbose_name='Origin')),
                ('en', models.CharField(max_length=255, verbose_name='English')),
                ('uz', models.CharField(max_length=255, null=True, verbose_name="O'zbekcha")),
                ('ru', models.CharField(max_length=255, null=True, verbose_name='Русский')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Xatoliklar',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('key', models.CharField(max_length=512, primary_key=True, serialize=False, verbose_name='Key')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, null=True, verbose_name='Device ip')),
                ('imei', models.CharField(max_length=50, null=True, verbose_name='Device imei')),
                ('mac', models.CharField(max_length=30, null=True, verbose_name='Device mac')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Device name')),
                ('firebase_reg_id', models.CharField(max_length=255, null=True, verbose_name='Device firebase_reg_id')),
                ('uuid', models.CharField(max_length=50, verbose_name='Device uuid')),
                ('version', models.CharField(max_length=20, null=True, verbose_name='Device version')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '10. Device',
            },
        ),
    ]
