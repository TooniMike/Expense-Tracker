# Generated by Django 5.0.1 on 2024-02-06 10:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_AddedBudgetTable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='password',
        ),
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]
