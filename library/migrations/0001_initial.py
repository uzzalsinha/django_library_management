# Generated by Django 4.2.3 on 2023-09-29 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('issued_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(default=library.models.expiry)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('roll_no', models.CharField(blank=True, max_length=3)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
