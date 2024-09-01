# Generated by Django 5.0.2 on 2024-08-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetchNews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pictureUrl',
            field=models.URLField(default='https://google.com', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(default='Generic', max_length=255),
            preserve_default=False,
        ),
    ]
