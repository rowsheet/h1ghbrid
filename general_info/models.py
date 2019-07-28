from django.db import models

# Create your models here.

class Something(models.Model):
	name = models.CharField(max_length=64,
		null=True, default=None, blank=True
	)
