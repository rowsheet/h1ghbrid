from django.db import models

# Create your models here.
class InfoSnippet(models.Model):
	name = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	text = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

# Create your models here.
class Newsletter(models.Model):
	name = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	email = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	phone_number = models.CharField(max_length=255,
		null=True, default=None, blank=True, unique=True
	)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class RaffleTicket(models.Model):
	ticket_number = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	info = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=True, default=None, blank=True, unique=False
	)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.ticket_number

class MMJNewsPost(models.Model):
	title = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	publication_name = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=True, default=None, blank=True, unique=False
	)
	url = models.CharField(max_length=512,
		null=True, default=None, blank=True, unique=False
	)
	img_url = models.CharField(max_length=512,
		null=True, default=None, blank=True, unique=False
	)
	text_preview = models.TextField(blank=True, null=True)
	publication_date = models.DateTimeField()
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class EventPublication(models.Model):
	title = models.CharField(max_length=255,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	text = models.TextField(blank=True, null=True)
	date = models.DateTimeField()
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
