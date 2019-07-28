from django.db import models
from django.template.defaultfilters import truncatechars
import datetime
from django_summernote.widgets import SummernoteInplaceWidget
from django.utils.html import strip_tags

class TextBitCategory(models.Model):
	name = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

class TextBit(models.Model):
	key = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	val = models.TextField(blank=True, null=True)
	text_bit_category = models.ForeignKey(
		"TextBitCategory",
		on_delete=models.SET_NULL,
		related_name = "text_bit_category",
		null=True, default=None, blank=True
	)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.key
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

class CustomJS(models.Model):
	key = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	val = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.key
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

class CustomCSS(models.Model):
	key = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	val = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.key
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

class PageTemplate(models.Model):
	key = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	val = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.key
	@property
	def val_change_list(self):
		return truncatechars(strip_tags(self.val), 32)

class Page(models.Model):
	title = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False
	)
	page_template = models.ForeignKey(
		"PageTemplate",
		on_delete=models.SET_NULL,
		related_name = "page_template",
		null=True, default=None, blank=True
	)
	leading_script = models.ForeignKey(
		"CustomJS",
		on_delete=models.SET_NULL,
		related_name = "leading_script",
		null=True, default=None, blank=True
	)
	trailing_script = models.ForeignKey(
		"CustomJS",
		on_delete=models.SET_NULL,
		related_name = "trailing_script",
		null=True, default=None, blank=True
	)
	leading_style = models.ForeignKey(
		"CustomCSS",
		on_delete=models.SET_NULL,
		related_name = "leading_style",
		null=True, default=None, blank=True
	)
	trailing_style = models.ForeignKey(
		"CustomCSS",
		on_delete=models.SET_NULL,
		related_name = "trailing_style",
		null=True, default=None, blank=True
	)
	aux_custom_template = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "aux_custom_template",
		null=True, default=None, blank=True
	)
	content_section_one = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_one",
		null=True, default=None, blank=True
	)
	content_section_two = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_two",
		null=True, default=None, blank=True
	)
	content_section_three = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_three",
		null=True, default=None, blank=True
	)
	content_section_four = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_four",
		null=True, default=None, blank=True
	)
	content_section_five = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_five",
		null=True, default=None, blank=True
	)
	content_section_six = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_six",
		null=True, default=None, blank=True
	)
	content_section_seven = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_seven",
		null=True, default=None, blank=True
	)
	content_section_eight = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_eight",
		null=True, default=None, blank=True
	)
	content_section_nine = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_nine",
		null=True, default=None, blank=True
	)
	content_section_ten = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_ten",
		null=True, default=None, blank=True
	)
	content_section_eleven = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_eleven",
		null=True, default=None, blank=True
	)
	content_section_twelve = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twelve",
		null=True, default=None, blank=True
	)
	content_section_thirteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_thirteen",
		null=True, default=None, blank=True
	)
	content_section_fourteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_fourteen",
		null=True, default=None, blank=True
	)
	content_section_fifteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_fifteen",
		null=True, default=None, blank=True
	)
	content_section_sixteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_sixteen",
		null=True, default=None, blank=True
	)
	content_section_seventeen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_seventeen",
		null=True, default=None, blank=True
	)
	content_section_eighteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_eighteen",
		null=True, default=None, blank=True
	)
	content_section_nineteen = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_nineteen",
		null=True, default=None, blank=True
	)
	content_section_twenty = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twenty",
		null=True, default=None, blank=True
	)
	content_section_twentyone = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentyone",
		null=True, default=None, blank=True
	)
	content_section_twentytwo = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentytwo",
		null=True, default=None, blank=True
	)
	content_section_twentythree = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentythree",
		null=True, default=None, blank=True
	)
	content_section_twentyfour = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentyfour",
		null=True, default=None, blank=True
	)
	content_section_twentyfive = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentyfive",
		null=True, default=None, blank=True
	)
	content_section_twentysix = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentysix",
		null=True, default=None, blank=True
	)
	content_section_twentyseven = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentyseven",
		null=True, default=None, blank=True
	)
	content_section_twentyeight = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentyeight",
		null=True, default=None, blank=True
	)
	content_section_twentynine = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_twentynine",
		null=True, default=None, blank=True
	)
	content_section_thirty = models.ForeignKey(
		"ContentSection",
		on_delete=models.SET_NULL,
		related_name = "content_section_thirty",
		null=True, default=None, blank=True
	)
	creation_timestamp = models.DateTimeField(auto_now=True)

class ContentSection(models.Model):
	name = models.CharField(max_length=64,
		# NOT NULL, UNIQUE, no default.
		null=False, default=None, blank=False, unique=True
	)
	# json_data = models.TextField(blank=True, null=True)
	template_data = models.TextField(blank=True, null=True)
	TABLE = 'table'
	JSON_ARRAY = 'json_array'
	JSON_OBJECT_AGG = 'json_object_agg'
	RESULT_TYPE = (
		(TABLE, 'table'),
		(JSON_ARRAY, 'json_array'),
		(JSON_OBJECT_AGG, 'json_object_agg'),
	)
	result_type = models.CharField(
		max_length=32,
		choices=RESULT_TYPE,
		# NOT NULL, no default.
		null=False, default=TABLE
	)
	sql_query = models.TextField(blank=True, null=True)
	creation_timestamp = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
