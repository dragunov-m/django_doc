# Generated by Django 4.1.5 on 2023-03-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='id',
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(max_length=3, primary_key=True, serialize=False),
        ),
    ]