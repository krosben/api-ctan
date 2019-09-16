from django.db import models
from .province import Province


class Town(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the town")
    province = models.ForeignKey(
        Province,
        related_name="towns",
        on_delete=models.CASCADE,
        help_text="Towns in the province",
    )
