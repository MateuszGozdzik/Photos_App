# Generated by Django 4.2 on 2023-04-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gravatar_link',
            field=models.URLField(default='https://www.xd.com'),
            preserve_default=False,
        ),
    ]
