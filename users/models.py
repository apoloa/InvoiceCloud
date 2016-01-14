# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class UsersNonce(models.Model):
    Owner = models.ForeignKey(User, related_name='users_nonce')  # Usuario
    CreateAt = models.DateTimeField(auto_now_add=True)  # Fecha de Creación
    Code = models.CharField(max_length=100)
