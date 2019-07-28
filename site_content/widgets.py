from django import forms
from django.utils.safestring import mark_safe
from django.template import Template, Context

import base64

class MyWidget(forms.Widget):
	def __init__(self, attrs=None, choices=()):
		super().__init__(attrs)

	def render(self, name, value, attrs=None, renderer=None):
		mode = "django"
		if self.attrs is not None:
			if "mode" in self.attrs:
				config_mode = self.attrs["mode"]
				if config_mode == "pgsql":
					mode = "pgsql"
				if config_mode == "css":
					mode = "css"
				if config_mode == "javascript":
					mode = "javascript"
		if value is None:
			value = ""
		value_decoded = base64.b64decode(value).decode('utf-8')
		return mark_safe(Template("""
<textarea name="{{ name }}" id="id_{{ name }}" style="display: none;"
>{{ value }}</textarea>
<br class="ace_pad">
<br class="ace_pad">
<div	name="{{ name }}"
	id="ace_id_{{ name }}"
	style="
		width: 100%;
		height: 400px;
	"
>{{ value_decoded }}</div>
<style>
.form-row ul.nav.nav-tabs {
	margin-left: 0px !important;
}
</style>
<script>
var ace_{{ name }} = ace.edit("ace_id_{{ name }}");
ace_{{ name }}.setTheme("ace/theme/monokai");
ace_{{ name }}.session.setMode("ace/mode/{{ mode }}");
ace_{{ name }}.setKeyboardHandler("ace/keyboard/vim");
ace.config.loadModule("ace/keyboard/vim", function(m) {
	var VimApi = require("ace/keyboard/vim").CodeMirror.Vim
	VimApi.defineEx("write", "w", function(cm, input) {
		content = cm.ace.getValue();
		selector_with_id = cm.ace.container.id.substr(4);
		selector_name = selector_with_id.substr(3)
		$("#" + cm.ace.container.id.substr(4)).html(btoa(content));
		$("#template_preview_" + selector_name + " .template_preview").html(content);
	})
})
</script>
		""").render(Context({
			"name": name,
			"value": value,
			"value_decoded": value_decoded,
			"mode": mode
		})))

# @TODO do previews in an iframe with base tempalte if you want.
#		if mode == "django":
#			return mark_safe(Template("""
#<textarea name="{{ name }}" id="id_{{ name }}" style="display: none;"
#>{{ value }}</textarea>
#<br class="ace_pad">
#<br class="ace_pad">
#<ul class="nav nav-tabs" role="tablist">
#	<li class="nav-item">
#		<a class="nav-link active" data-toggle="tab" href="#template_editor_{{ name }}">
#			Template Editor
#		</a>
#	</li>
#	<li class="nav-item">
#		<a class="nav-link" data-toggle="tab" href="#template_preview_{{ name }}">
#			Template Preview
#		</a>
#	</li>
#</ul>
#<div class="tab-content">
#	<div id="template_editor_{{ name }}" class="tab-pane active"><br>
#		<div	name="{{ name }}"
#			id="ace_id_{{ name }}"
#			style="
#				width: 100%;
#				height: 400px;
#			"
#		>{{ value_decoded }}</div>
#	</div>
#	<div id="template_preview_{{ name }}" class="tab-pane fade"><br>
#		<div	
#			style="
#				width: 100%;
#				height: 400px;
#			"
#			class="template_preview"
#		>{{ value_decoded | safe }}</div>
#	</div>
#</div>
#<style>
#.form-row ul.nav.nav-tabs {
#	margin-left: 0px !important;
#}
#</style>
#<script>
#var ace_{{ name }} = ace.edit("ace_id_{{ name }}");
#ace_{{ name }}.setTheme("ace/theme/monokai");
#ace_{{ name }}.session.setMode("ace/mode/{{ mode }}");
#ace_{{ name }}.setKeyboardHandler("ace/keyboard/vim");
#ace.config.loadModule("ace/keyboard/vim", function(m) {
#	var VimApi = require("ace/keyboard/vim").CodeMirror.Vim
#	VimApi.defineEx("write", "w", function(cm, input) {
#		content = cm.ace.getValue();
#		selector_with_id = cm.ace.container.id.substr(4);
#		selector_name = selector_with_id.substr(3)
#		$("#" + cm.ace.container.id.substr(4)).html(btoa(content));
#		$("#template_preview_" + selector_name + " .template_preview").html(content);
#	})
#})
#</script>
#			""").render(Context({
#				"name": name,
#				"value": value,
#				"value_decoded": value_decoded,
#				"mode": mode
#			})))
