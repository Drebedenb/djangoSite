# Generated by Django 3.1.5 on 2022-05-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_likebutton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('anons', models.CharField(max_length=250, verbose_name='Anounse')),
                ('full_text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(verbose_name='Date of publication')),
            ],
        ),
        migrations.RemoveField(
            model_name='likebutton',
            name='likes',
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.DeleteModel(
            name='LikeButton',
        ),
    ]
