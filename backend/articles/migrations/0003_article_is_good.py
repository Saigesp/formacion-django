# Generated by Django 4.1.5 on 2023-01-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_alter_article_pub_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_good",
            field=models.BooleanField(default=True),
        ),
    ]
