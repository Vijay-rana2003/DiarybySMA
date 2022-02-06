# Generated by Django 4.0.2 on 2022-02-06 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contactuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='mydiary',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('Description', models.TextField()),
                ('Short_Description', models.CharField(max_length=300)),
                ('Slug', models.CharField(max_length=300)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
