from django.db import models
from django.conf import settings


class todo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    task = models.TextField()

    def __str__(self):
        return self.task

