# Generated by Django 5.0.1 on 2024-02-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
