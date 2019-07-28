from django import forms
from django.utils.safestring import mark_safe
from django.template import Template, Context
from .utils import get_guid 

import base64

# @TODO for later.
class JSONDataWidget(forms.Widget):
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
		value_decoded = base64.b64decode(value).decode('utf-8', 'ignore')
		# value_decoded = base64.b64decode(value).decode('UTF-16LE')
		field_guid = get_guid()
		return mark_safe(Template("""
<h1>{{ field_guid }}</h1>
<textarea name="{{ name }}" id="id_{{ name }}" class="{{ field_guid }}"
>{{ value }}</textarea>
<style>
table.jsoneditor-search {
    border-radius: 0px;
    box-shadow: none;
}
table.jsoneditor-search * {
    border: none !important;
    box-shadow: none;
}
div#jsoneditor * {
    border-radius: 0px;
    box-shadow: none;
}
.jsoneditor-menu {
    background: #02a8f4 !important;
}
div#jsoneditor {
    padding-top: 43px;
}
.jsoneditor.jsoneditor-mode-tree {
    border: none;
    background: whitesmoke;
}
</style>
<button class="btn btn-primary">Save</button>
<div id="jsoneditor" style="height: 400px;"></div>
<script>
$(document).ready(function() {
	// create the editor
	var container = document.getElementById("jsoneditor");
	var options = {};
	var editor = new JSONEditor(container, options);

	// set json
	var json = {
{{ value_decoded | safe }}
	};
	editor.set(json);

	// get json
	var json = editor.get();
});
</script>
		""").render(Context({
			"name": name,
			"value": value,
			"value_decoded": value_decoded,
			"mode": mode,
			"field_guid": field_guid 
		})))

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
		value_decoded = base64.b64decode(value).decode('utf-8', 'ignore')
		# value_decoded = base64.b64decode(value).decode('UTF-16LE')
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
		$("#" + cm.ace.container.id.substr(4)).html(encodeURI(btoa(content)));
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
