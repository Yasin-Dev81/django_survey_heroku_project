from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return "%s - %s [%s]" % (
            self.first_name,
            self.last_name,
            self.username,
        )

    def get_absolute_url(self):
        return reverse('home_url')
