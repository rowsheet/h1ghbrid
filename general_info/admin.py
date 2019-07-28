from django.contrib import admin

# Register your models here.

from .models import Something

class SomethingAdmin(admin.ModelAdmin):
	# change_form_template = 'admin/general_info/extend.html'
	some_data = "SOME_DATA"

	def change_view(self, request, object_id, form_url='', extra_context=None):
		extra_context = extra_context or {}
		extra_context['custom_changeview_top'] = '<h1>Custom Changeview Top</h1>'
		extra_context['custom_changeview_bottom'] = '<h1>Custom Changeview Bottom</h1>'
		return super(SomethingAdmin, self).change_view(
			request, object_id, form_url, extra_context=extra_context,
		)
	def add_view(self, request, form_url='', extra_context=None):
		extra_context = extra_context or {}
		extra_context['custom_addview_top'] = '<h1>Custom Addview Top</h1>'
		extra_context['custom_addview_bottom'] = '<h1>Custom Addview Bottom</h1>'
		return super(SomethingAdmin, self).add_view(
			request, form_url, extra_context=extra_context,
		)
	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
		extra_context['custom_changelist_top'] = '<h1>Custom Changelistview Top</h1>'
		extra_context['custom_changelist_bottom'] = '<h1>Custom Changelistview Bottom</h1>'
		return super(SomethingAdmin, self).changelist_view(
			request, extra_context=extra_context,
		)
	# change_list_template = 'admin/preview_template.html'
	pass
admin.site.register(Something, SomethingAdmin)
