# Generated by Django 5.0.2 on 2024-03-12 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='login',
            new_name='username',
        ),
    ]
