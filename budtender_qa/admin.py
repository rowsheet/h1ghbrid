from django.contrib import admin

from .models import BudtenderReviews

class BudtenderReviewsAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"product",
		"creation_timestamp"
	)
admin.site.register(BudtenderReviews, BudtenderReviewsAdmin)
