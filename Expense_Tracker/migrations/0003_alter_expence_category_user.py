# Generated by Django 4.2.4 on 2023-08-24 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Expense_Tracker', '0002_expence_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expence_category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
