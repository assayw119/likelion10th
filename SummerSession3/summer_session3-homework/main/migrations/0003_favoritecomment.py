# Generated by Django 4.0.6 on 2022-07-26 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_post_favo_image_remove_post_favo_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_comments', to='main.favorite')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]