from django import forms

from .models import TextBit
from .models import ContentSection
from .models import CustomCSS 
from .models import CustomJS
from .models import PageTemplate

from .widgets import MyWidget 

class TextBitAdminForm(forms.ModelForm):
	class Meta:
		model = TextBit
		widgets = {
			'val': MyWidget(attrs={"mode": "django"}),
		}
		fields = "__all__"

class ContentSectionAdminForm(forms.ModelForm):
	class Meta:
		model = ContentSection
		widgets = {
			'sql_query': MyWidget(attrs={"mode": "pgsql"}),
			'template_data': MyWidget(attrs={"mode": "html"}),
		}
		fields = "__all__"

class CustomCSSAdminForm(forms.ModelForm):
	class Meta:
		model = CustomCSS
		widgets = {
			'val': MyWidget(attrs={"mode": "css"}),
		}
		fields = "__all__"

class CustomJSAdminForm(forms.ModelForm):
	class Meta:
		model = CustomJS
		widgets = {
			'val': MyWidget(attrs={"mode": "javascript"}),
		}
		fields = "__all__"

class PageTemplateAdminForm(forms.ModelForm):
	class Meta:
		model = PageTemplate
		widgets = {
			'val': MyWidget(attrs={
				"mode": "django",
				"preview": False
			}),
		}
		fields = "__all__"
