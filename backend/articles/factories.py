# -*- coding: utf-8 -*-
import factory
from factory import fuzzy
from django.contrib.auth.models import User
from . import models


class UserFactory(factory.django.DjangoModelFactory):
    username = fuzzy.FuzzyText(length=12)
    email = fuzzy.FuzzyText(length=24, suffix="@test.com")

    class Meta:
        model = User

class CommentFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("articles.factories.UserFactory")
    body = fuzzy.FuzzyText(length=100)

    class Meta:
        model = models.Comment
