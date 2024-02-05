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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
