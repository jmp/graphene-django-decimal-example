from django.db import models


class Dummy(models.Model):
    foo = models.DecimalField(max_digits=10, decimal_places=2)
