# Generated by Django 3.1.5 on 2022-05-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20220516_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'One new article', 'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
    ]
