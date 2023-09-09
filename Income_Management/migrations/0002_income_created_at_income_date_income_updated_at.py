# Generated by Django 4.2.4 on 2023-09-09 01:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Income_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]