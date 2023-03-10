# Generated by Django 4.1.5 on 2023-02-25 15:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 18, 14, 29, 434235)),
        ),
        migrations.AddField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 18, 14, 29, 433212)),
        ),
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='default title', max_length=20),
        ),
    ]
