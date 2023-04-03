# Generated by Django 4.1.7 on 2023-03-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
                ('mobile', models.CharField(max_length=20)),
                ('is_expired', models.BooleanField(default=False)),
                ('tries', models.SmallIntegerField(default=0)),
                ('extra', models.JSONField(default={})),
                ('is_verified', models.BooleanField(default=False)),
                ('step', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
