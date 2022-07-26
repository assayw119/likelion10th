# Generated by Django 4.0.6 on 2022-07-26 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favo_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='favo_title',
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('favo_title', models.CharField(max_length=100)),
                ('favo_image', models.ImageField(blank=True, null=True, upload_to='favorites/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
