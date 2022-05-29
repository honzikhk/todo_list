from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


def one_week_later():
    return timezone.now() + timedelta(days=7)


def tomorrow():
    return timezone.now() + timedelta(days=1)


class Task(models.Model):
    PRIORITY_HIGH = "Must do"
    PRIORITY_NORMAL = "Should do"
    PRIORITY_LOW = "Nice to do"

    PRIORITY_CHOICES = (
        (PRIORITY_HIGH, "Must do"),
        (PRIORITY_NORMAL, "Should do"),
        (PRIORITY_LOW, "Nice to do")
    )

    CATEGORY_FAMILY = "family"
    CATEGORY_WORK = "work"
    CATEGORY_GARDEN = "garden"
    CATEGORY_HOUSEHOLD = "household"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = (
        (CATEGORY_FAMILY, "Family"),
        (CATEGORY_WORK, "Work"),
        (CATEGORY_GARDEN, "Garden"),
        (CATEGORY_HOUSEHOLD, "Household"),
        (CATEGORY_OTHER, "Other")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=25)
    category = models.CharField(choices=CATEGORY_CHOICES, default="other", max_length=21)
    description = models.TextField(null=True, blank=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default="normal", max_length=15)  # there must be a "max_length" attribute
    to_do = models.DateTimeField(default=tomorrow)
    dead_line = models.DateTimeField(default=one_week_later)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name[:30]

    # class Meta:
    #     ordering = ["completed"]
