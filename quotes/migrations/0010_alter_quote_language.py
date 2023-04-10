# Generated by Django 4.2 on 2023-04-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0009_alter_quote_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("EN", "English"), ("PL", "Polish")],
                max_length=2,
                null=True,
            ),
        ),
    ]
