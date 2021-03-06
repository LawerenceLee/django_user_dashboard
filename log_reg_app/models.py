# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ID: {}\nFirst: {}\nLast: {}\nEmail: {}\nPassword: {}\
        ".format(
            self.id, self.first_name, self.last_name,
            self.email, self.password,
        )

    def __repr__(self):
        return "ID: {}, First: {}, Last: {}, Email: {}, Password: {}\
        ".format(
            self.id, self.first_name, self.last_name,
            self.email, self.password,
        )

