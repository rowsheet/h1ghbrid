from django.contrib import admin
from .models import InfoSnippet
from .models import Newsletter
from .models import MMJNewsPost 
from .models import EventPublication 
from .models import RaffleTicket
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class InfoSnippetAdmin(SummernoteModelAdmin):
	search_fields = (
		"name",
		"text",
	)
	list_display = (
		"name",
#		"text",
		"creation_timestamp",
	)
	# def _text(self, obj):
	#	return format_row_code_preview(obj.id, obj.text, "text", "django")
	# _creation_timestamp.admin_order_field = 'creation_timestamp'
	# _text.admin_order_field = 'text'
admin.site.register(InfoSnippet, InfoSnippetAdmin)

class NewsletterAdmin(admin.ModelAdmin):
	search_fields = (
		"name",
		"email",
		"phone_number",
	)
	list_display = (
		"name",
		"email",
		"phone_number",
		"creation_timestamp",
	)
admin.site.register(Newsletter, NewsletterAdmin)

class RaffleTicketAdmin(admin.ModelAdmin):
	search_fields = (
		"ticket_number",
		"info",
	)
	list_display = (
		"ticket_number",
		"info",
		"creation_timestamp",
	)
admin.site.register(RaffleTicket, RaffleTicketAdmin)

class MMJNewsPostAdmin(admin.ModelAdmin):
	search_fields = (
		"title",
		"publication_name",
		"url",
		"img_url",
		"text_preview",
		"publication_date",
		"creation_timestamp"
	)
	list_display = (
		"_title",
		"publication_name",
		"publication_date",
		"_img_url",
		"_text_preview",
		"_url",
		"creation_timestamp"
	)
	def _title(self, obj):
		return mark_safe("""
		<div style="width: 200px;">%s</div>
		""" % obj.title)
	def _text_preview(self, obj):
		if obj.text_preview is not None:
			return mark_safe("""
			<div style="width: 300px;">%s</div>
			""" %
			obj.text_preview[0:200] + "...")
		return None
	def _url(self, obj):
		if obj.url is not None:
			return mark_safe("""
			<a href="%s">%s</a>
			""" % (
				obj.url,
				obj.url[0:32] + "...",
			))
		return None
	def _img_url(self, obj):
		if obj.img_url is not None:
			return mark_safe("""
			<img src="%s" style="height: 100px; width: 100px; object-fit: cover;">
			""" % 
			obj.img_url)
		return None
admin.site.register(MMJNewsPost, MMJNewsPostAdmin)

class EventPublicationAdmin(SummernoteModelAdmin):
	search_fields = (
		"title",
		"text",
		"date",
	)
	list_display = (
		"title",
		"date",
		"creation_timestamp",
	)
	# def _text(self, obj):
	#	return format_row_code_preview(obj.id, obj.text, "text", "django")
	# _creation_timestamp.admin_order_field = 'creation_timestamp'
	# _text.admin_order_field = 'text'
admin.site.register(EventPublication, EventPublicationAdmin)
