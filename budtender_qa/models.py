from django.conf import settings
from django.db import models
from tgtree import models as tgtree_models 

class BudtenderReviews(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True, default=None, blank=True
	)
	product = models.ForeignKey(
		tgtree_models.Product,
		on_delete=models.SET_NULL,
		null=True, default=None, blank=True
	)
	creation_timestamp = models.DateTimeField(auto_now=True)
