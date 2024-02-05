import uuid

from django.conf import settings
from django.db import models


class Vacation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    id = models.AutoField(primary_key=True)
