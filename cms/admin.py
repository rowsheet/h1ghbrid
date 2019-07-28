from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django_summernote.admin import SummernoteModelAdmin
from django.template import Template, Context
from django.db import models
from django import forms

from jet.admin import CompactInline

import base64

from .models import Page
from .models import ContentSection
from .models import TextBit
from .models import TextBitCategory
from .models import CustomJS 
from .models import CustomCSS 
from .models import PageTemplate

from .widgets import MyWidget 

from .forms import TextBitAdminForm
from .forms import ContentSectionAdminForm
from .forms import CustomCSSAdminForm 
from .forms import CustomJSAdminForm 
from .forms import PageTemplateAdminForm 

def format_creation_timestamp(value):
	if value is None:
		return mark_safe("<code style='color: red;'>NULL</code>")
	if value == "":
		return mark_safe("<code style='color: red;'>NULL</code>")
	return mark_safe("<code><nobr class='code_primary'>" + str(value) + "</nobr></code>")

def format_row_code_preview(obj_id, code_data, col_key, mode = "django"):
	if code_data == "":
		return "-"
	unique_suffix = str(obj_id) + "_" + col_key
	return mark_safe("""
<div 
class="code_preview jet_collapse"
id="ace_content_section_%s"
onclick="toggle_code_preview(this.id)"
>%s</div>
<script>
var ace_content_section_%s = ace.edit("ace_content_section_%s");
ace_content_section_%s.setTheme("ace/theme/monokai");
ace_content_section_%s.session.setMode("ace/mode/%s");
ace_content_section_%s.setReadOnly(true);
ace_content_section_%s.setAutoScrollEditorIntoView(true);
editors["ace_content_section_%s"] = ace_content_section_%s;
</script>
	""" % (
		unique_suffix,
		escape(base64.b64decode(code_data).decode("utf-8", "ignore")),
		# escape(base64.b64decode(code_data)),
		unique_suffix,
		unique_suffix,
		unique_suffix,
		unique_suffix,
		mode,
		unique_suffix,
		unique_suffix,
		unique_suffix,
		unique_suffix,
	))	

class CustomJSAdmin(admin.ModelAdmin):
	form = CustomJSAdminForm
	search_fields = (
		"key",
		"val",
	)
	list_display = (
		"key",
		"_val",
		"_creation_timestamp",
	)
	def _val(self, obj):
		return format_row_code_preview(obj.id, obj.val, "val", "javascript")
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_creation_timestamp.admin_order_field = 'creation_timestamp'
	_val.admin_order_field = 'val'
admin.site.register(CustomJS, CustomJSAdmin)

class CustomCSSAdmin(admin.ModelAdmin):
	form = CustomCSSAdminForm
	search_fields = (
		"key",
		"val",
	)
	list_display = (
		"key",
		"_val",
		"_creation_timestamp",
	)
	def _val(self, obj):
		return format_row_code_preview(obj.id, obj.val, "val", "css")
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_creation_timestamp.admin_order_field = 'creation_timestamp'
	_val.admin_order_field = 'val'
admin.site.register(CustomCSS, CustomCSSAdmin)

class PageTemplateAdmin(admin.ModelAdmin):
	form = PageTemplateAdminForm
	search_fields = (
		"key",
		"val",
	)
	list_display = (
		"key",
		"_val",
		"_creation_timestamp",
	)
	def _val(self, obj):
		return format_row_code_preview(obj.id, obj.val, "val", "django")
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_creation_timestamp.admin_order_field = 'creation_timestamp'
	_val.admin_order_field = 'val'
admin.site.register(PageTemplate, PageTemplateAdmin)

class TextBitAdmin(admin.ModelAdmin):
	form = TextBitAdminForm
	search_fields = (
		"key",
		"val",
		"text_bit_category__name",
	)
	list_display = (
		"key",
		"_val",
		"text_bit_category",
		"_creation_timestamp",
	)
	def _val(self, obj):
		return format_row_code_preview(obj.id, obj.val, "val", "django")
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_creation_timestamp.admin_order_field = 'creation_timestamp'
	_val.admin_order_field = 'val'
admin.site.register(TextBit, TextBitAdmin)

class ContentSectionAdmin(admin.ModelAdmin):
	form = ContentSectionAdminForm
	search_fields = (
		"name",
		"creation_timestamp",
	)
	list_display = (
		"_name",
		"_creation_timestamp",
	#	"_json_data",
		"_template_data",
		"_sql_query",
	)
	def _name(self, obj):
		return mark_safe("<nobr>" + obj.name + "</nobr>")
	# def _json_data(self, obj):
	#	return format_row_code_preview(obj.id, obj.sql_query, "sql_query", "pgsql")
	def _sql_query(self, obj):
		return format_row_code_preview(obj.id, obj.sql_query, "sql_query", "pgsql")
	def _template_data(self, obj):
		return format_row_code_preview(obj.id, obj.template_data, "template_data", "django")
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_creation_timestamp.admin_order_field = 'creation_timestamp'
	_name.admin_order_field = 'name'
	_template_data.admin_order_field = 'template_data'
	_sql_query.admin_order_field = 'sql_query'
admin.site.register(ContentSection, ContentSectionAdmin)

class PageAdmin(admin.ModelAdmin):
	list_display = (
		"title",
		"_preview",
		"page_template",
		"leading_script",
		"trailing_script",
		"leading_style",
		"trailing_style",
		"aux_custom_template",
		"content_section_one",
		"content_section_two",
		"content_section_three",
		"content_section_four",
		"content_section_five",
		"content_section_six",
		"content_section_seven",
		"content_section_eight",
		"content_section_nine",
		"content_section_ten",
		"content_section_eleven",
		"content_section_twelve",
		"content_section_thirteen",
		"content_section_fourteen",
		"content_section_fifteen",
		"content_section_sixteen",
		"content_section_seventeen",
		"content_section_eighteen",
		"content_section_nineteen",
		"content_section_twenty",
		"content_section_twentyone",
		"content_section_twentytwo",
		"content_section_twentythree",
		"content_section_twentyfour",
		"content_section_twentyfive",
		"content_section_twentysix",
		"content_section_twentyseven",
		"content_section_twentyeight",
		"content_section_twentynine",
		"content_section_thirty",
		"creation_timestamp",
	)
	def _preview(self, obj):
		return mark_safe("""
<script>
function add_iframe(which_modal) {
	console.log(which_modal);
	$('#preview_' + which_modal + ' .modal-body').html("<iframe style='width: 100%; height: 75vh;' src='/" + which_modal + "' iframe>");
}
</script>
<button onclick="add_iframe('""" + obj.title + """')" type="button" style="background: #02a9f4;" class="button" data-toggle='modal' data-target='#preview_""" + obj.title + """'>preview</button>
<div class="modal fade" id='preview_""" + obj.title + """' tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	<div class="modal-dialog modal-xl" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
				<button type="button" class="btn btn-primary">Save changes</button>
			</div>
		</div>
	</div>
</div>
		""")
admin.site.register(Page, PageAdmin)

"""
class TextBitInline(admin.TabularInline):
	model = TextBit

class TextBitCategoryAdmin(admin.ModelAdmin):
	inlines = (
		TextBitInline,
	)
	list_display = (
		"name",
		"_creation_timestamp",
		"_count",
	)
	def get_queryset(self, request):
		return TextBitCategory.objects.annotate(count=models.Count('text_bit_category'))
	def _count(self, obj):
		return obj.count
	def _creation_timestamp(self, obj):
		return format_creation_timestamp(obj.creation_timestamp)
	_count.admin_order_field = 'count'
	_creation_timestamp.admin_order_field = 'creation_timestamp'
admin.site.register(TextBitCategory, TextBitCategoryAdmin)
"""
