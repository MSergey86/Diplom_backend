# Generated by Django 5.0.2 on 2024-03-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('admin_or_not', models.BooleanField(default=False)),
                ('url_user', models.URLField(null=True, unique=True)),
            ],
        ),
    ]
