from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the province")
