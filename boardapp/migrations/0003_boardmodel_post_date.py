# Generated by Django 4.2.7 on 2023-12-03 09:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_alter_boardmodel_good_alter_boardmodel_read_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]