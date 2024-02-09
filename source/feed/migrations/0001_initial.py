# Generated by Django 5.0.1 on 2024-01-15 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images', verbose_name='Картинка')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст публикации')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr_posts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500, verbose_name='Текст отзыва')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('date_edit', models.DateField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a_comment', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_comment', to='feed.postmodel', verbose_name='Продукт')),
            ],
        ),
    ]
