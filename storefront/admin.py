from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

# Register your models here.
from .models import Product
from .models import ProductTag
from .models import EmployeeProductQA 
from .models import ProductPromotion
from .models import ProductPromotionCategory
from .models import MembershipPlan 
from .models import UserMembership 

class UserMembershipAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'plan',
		'start_date',
		'end_date',
		'creation_timestamp',
		'last_changed_timestamp',
	)
	search_fields = (
		'user',
		'plan',
		'start_date',
		'end_date',
		'creation_timestamp',
		'last_changed_timestamp',
	)
admin.site.register(UserMembership, UserMembershipAdmin)

class MembershipPlanAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'price',
		'period',
		'short_description',
		'long_description',
		'creation_timestamp',
		'last_changed_timestamp',
	)
	search_fields = (
		'name',
		'price',
		'period',
		'short_description',
		'long_description',
		'creation_timestamp',
		'last_changed_timestamp',
	)
admin.site.register(MembershipPlan, MembershipPlanAdmin)

class EmployeeProductQAAdmin(admin.ModelAdmin):
	list_display = (
		"_review_item",
		"_assigned",
		"_completed",
		"_back_log",
		"user",
		"product",
		"date_assigned",
		"date_submitted",
		"date_due",
		"comments",
		"rating_one",
		"rating_two",
		"creation_timestamp",
	)
	def get_queryset(self, request):
		query_set = super(EmployeeProductQAAdmin, self).get_queryset(request)
		if not request.user.groups.filter(name="product_admin").exists():
			return query_set.filter(user=request.user).exclude(date_assigned__isnull=True)
		return query_set.filter()
	def format_bool(self, data):
		if data == True:
			return mark_safe("<div style='color: green;'>" + str(data) + "</div>")
		return mark_safe("<div style='color: red;'>" + str(data) + "</div>")
	def _review_item(self, obj):
		user_name = ""
		if obj.user is None:
			user_name = "NA"
		else:
			user_name = obj.user.username
		product_name = ""
		if obj.product is None:
			product_name = "NA"
		else:
			product_name = obj.product.name
		return mark_safe("<nobr>" + user_name + " => " + product_name + "</nobr>")
	def _assigned(self, obj):
		if obj.date_assigned is None:
			return self.format_bool(False)
		return self.format_bool(True)
	def _completed(self, obj):
		if (obj.date_submitted is not None) and (obj.comments is not None) and (obj.rating_one is not None) and (obj.rating_two is not None):
			return self.format_bool(True)
		return self.format_bool(False)
	def _back_log(self, obj):
		if obj.date_due is not None:
			if obj.date_due < timezone.localtime():
				return self.format_bool(True)
		return self.format_bool(False)

admin.site.register(EmployeeProductQA, EmployeeProductQAAdmin)

def format_bool(value):
	if (value):
		return mark_safe("""
			<div class="td_true">True</div>
		""")
	return mark_safe("""
		<div class="td_false">False</div>
	""")

def format_tags(tags):
	if tags is None:
		return mark_safe("""
			<div class="no_tags">No tags</div>
		""")
	tags_html = ",".join([
		("""
		<div class="has_tags"><nobr>%s</nobr></div>
		""" % (tag.name)) for tag in tags.all()
	]) 
	if tags_html == "":
		return mark_safe("""
			<div class="no_tags">No tags</div>
		""")
	return mark_safe(tags_html)

class ProductTagAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'description',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
	search_fields = (
		'name',
		'description',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
admin.site.register(ProductTag, ProductTagAdmin)


class ProductPromotionCategoryAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'description',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
	search_fields = (
		'name',
		'description',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
admin.site.register(ProductPromotionCategory, ProductPromotionCategoryAdmin)

class ProductPromotionAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'product',
		'category',
		'_tags',
		'_active',
		'description',
		'start_date',
		'end_date',
		'promo_code',
		'selling_price',
		'discount',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
	search_fields = (
		'title',
		'category__name',
		'description',
		'start_date',
		'end_date',
		'promo_code',
		'selling_price',
		'discount',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)

	def _active(self, obj):
		return format_bool(obj.active)

	def _tags(self, obj):
		return format_tags(obj.tags)
admin.site.register(ProductPromotion, ProductPromotionAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'description',
		'_adilis_active',
		'_adilas_import_timestamp',
		'_adilas_import_error',
		'_visible',
		'_for_sale',
		'_discontinued',
		'_tags',
		'parent_product',
		'_vendor',
		'upc',
		'vendor_code',
	# 	'man_part_number',
	# 	'htc_number',

	# 	'model',
	# 	'brand',
	# 	'text_document',
	# 	'spec_kv',
		'details_kv',

	# 	'msrp',
		'base_price',
		'price',

		'_image',
		'uofm',
		'inventory',
		'bin_date',
		'weight',
		'category',
		'creation_timestamp',
		'last_changed_timestamp',
		'job_timestamp'
	)
	search_fields = (
		'vendor',
		'name',
		'upc',
		'base_price',
		'price',
		'uofm',
		'inventory',
		'bin_date',
		'weight',
		'category',
		'description',
		'creation_timestamp'
	)

	def _visible(self, obj):
		return format_bool(obj.visible)

	def _for_sale(self, obj):
		return format_bool(obj.for_sale)

	def _discontinued(self, obj):
		return format_bool(obj.discontinued)

	def _adilis_active(self, obj):
		return format_bool(obj.adilas_active)

	def _adilas_import_timestamp(self, obj):
		return mark_safe("""
		<code>%s</code>
		""" % obj.adilas_import_timestamp)

	def _adilas_import_error(self, obj):
		return format_bool(obj.adilas_import_error)

	def _vendor(self, obj):
		return mark_safe("""
			<div style='width: 200px'>%s</div>
		""" % obj.vendor)

	def _image(self, obj):
		image_links_html = "".join([
			("""
			<a target="_blank" rel="noopener noreferrer" href="%s">
				<img 
					style="height: 75px;width: 75px;object-fit: cover;"
					src="%s"/>
			</a>
			""" % (img.gcloud_img_src, img.gcloud_img_src)) for img in obj.image.all()
		]) 
		if len(obj.image.all()) == 0:
			image_links_html = "<div class='admin_no_images_message'>No images</div>"
		return mark_safe("""
		<div class="admin_table_image_list_container">
			<div class="admin_table_image_list_content">
			%s 
			</div>
		</div>
		""" % image_links_html)
	def _tags(self, obj):
		return format_tags(obj.tags)
admin.site.register(Product, ProductAdmin)
