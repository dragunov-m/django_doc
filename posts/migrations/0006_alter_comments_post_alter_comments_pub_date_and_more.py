# Generated by Django 4.1.5 on 2023-02-27 18:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_posts_slug_alter_comments_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 21, 54, 38, 561205)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 21, 54, 38, 560124)),
        ),
    ]