# -*- coding: utf-8 -*-
from django.db import migrations


def apply_migration(apps, *args):
    UserModel = apps.get_model("auth", "user")
    UserModel.objects.create(username="editor", email="editor@gmail.com")


def revert_migration(apps, *args):
    UserModel = apps.get_model("auth", "user")
    UserModel.objects.filter(username="editor").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_article_edit_date"),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]
