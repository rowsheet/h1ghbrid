from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import Template, Context
from django.http import HttpResponse
from django.db import connection
from django.conf import settings
import traceback
from .models import Page 
from .models import ContentSection
from css_html_js_minify import html_minify, js_minify, css_minify
from django.http import HttpResponse
import re
import htmlmin
import json
import base64

def mobile_landing(request):
	carousel_items = CarouselRow.objects.all()
	return render(request, "site_content/mobile_landing.html", {
	})

def home_page(request, page="home"):
	return dynamic_page(request, page)

def build_static_style(request, template_string):
	try:
		if template_string is None:
			return ""
		if template_string == "":
			return ""
		template_string = base64.b64decode(template_string).decode('utf-8')
		template = Template(template_string)
		context = Context({
			"request": request,
		})
		return css_minify(template.render(context),comments=False)
	except Exception as ex:
		print(str(ex))
		return "/* Unable to render style: %s */" % str(ex)

def build_static_script(request, template_string):
	try:
		if template_string is None:
			return ""
		if template_string == "":
			return ""
		template_string = base64.b64decode(template_string).decode('utf-8')
		template = Template(template_string)
		context = Context({
			"request": request,
		})
		return js_minify(template.render(context))
	except Exception as ex:
		print(str(ex))
		return "console.log('Unable to render script: %s');" % str(ex)

def dynamic_page(request, page="home"):
	try:
		page = Page.objects.get(title=page)
		leading_script = ""
		if page.leading_script is not None:
			leading_script = build_static_script(request, page.leading_script.val)
		trailing_script = ""
		if page.trailing_script is not None:
			trailing_script = build_static_script(request, page.trailing_script.val)
		leading_style = ""
		if page.leading_style is not None:
			leading_style = build_static_style(request, page.leading_style.val)
		trailing_style = ""
		if page.trailing_style is not None:
			trailing_style = build_static_style(request, page.trailing_style.val)
		aux_custom_template = ""
		if page.aux_custom_template is not None:
			aux_custom_template += build_custom_template(request, page.aux_custom_template)
		html = ""
		print("DP")
		content_section_one = ""
		if page.content_section_one is not None:
			content_section_one = build_custom_template(request, page.content_section_one)
			html += content_section_one
		content_section_two = ""
		if page.content_section_two is not None:
			content_section_two = build_custom_template(request, page.content_section_two)
			html += content_section_two
		content_section_three = ""
		if page.content_section_three is not None:
			content_section_three = build_custom_template(request, page.content_section_three)
			html += content_section_three
		content_section_four = ""
		if page.content_section_four is not None:
			content_section_four = build_custom_template(request, page.content_section_four)
			html += content_section_four
		content_section_five = ""
		if page.content_section_five is not None:
			content_section_five = build_custom_template(request, page.content_section_five)
			html += content_section_five
		content_section_six = ""
		if page.content_section_six is not None:
			content_section_six = build_custom_template(request, page.content_section_six)
			html += content_section_six
		content_section_seven = ""
		if page.content_section_seven is not None:
			content_section_seven = build_custom_template(request, page.content_section_seven)
			html += content_section_seven
		content_section_eight = ""
		if page.content_section_eight is not None:
			content_section_eight = build_custom_template(request, page.content_section_eight)
			html += content_section_eight
		content_section_nine = ""
		if page.content_section_nine is not None:
			content_section_nine = build_custom_template(request, page.content_section_nine)
			html += content_section_nine
		content_section_ten = ""
		if page.content_section_ten is not None:
			content_section_ten = build_custom_template(request, page.content_section_ten)
			html += content_section_ten
		content_section_eleven = ""
		if page.content_section_eleven is not None:
			content_section_eleven = build_custom_template(request, page.content_section_eleven)
			html += content_section_eleven
		content_section_twelve = ""
		if page.content_section_twelve is not None:
			content_section_twelve = build_custom_template(request, page.content_section_twelve)
			html += content_section_twelve
		content_section_thirteen = ""
		if page.content_section_thirteen is not None:
			content_section_thirteen = build_custom_template(request, page.content_section_thirteen)
			html += content_section_thirteen
		content_section_fourteen = ""
		if page.content_section_fourteen is not None:
			content_section_fourteen = build_custom_template(request, page.content_section_fourteen)
			html += content_section_fourteen
		content_section_fifteen = ""
		if page.content_section_fifteen is not None:
			content_section_fifteen = build_custom_template(request, page.content_section_fifteen)
			html += content_section_fifteen
		content_section_sixteen = ""
		if page.content_section_sixteen is not None:
			content_section_sixteen = build_custom_template(request, page.content_section_sixteen)
			html += content_section_sixteen
		content_section_seventeen = ""
		if page.content_section_seventeen is not None:
			content_section_seventeen = build_custom_template(request, page.content_section_seventeen)
			html += content_section_seventeen
		content_section_eighteen = ""
		if page.content_section_eighteen is not None:
			content_section_eighteen = build_custom_template(request, page.content_section_eighteen)
			html += content_section_eighteen
		content_section_nineteen = ""
		if page.content_section_nineteen is not None:
			content_section_nineteen = build_custom_template(request, page.content_section_nineteen)
			html += content_section_nineteen
		content_section_twenty = ""
		if page.content_section_twenty is not None:
			content_section_twenty = build_custom_template(request, page.content_section_twenty)
			html += content_section_twenty
		content_section_twentyone = ""
		if page.content_section_twentyone is not None:
			content_section_twentyone = build_custom_template(request, page.content_section_twentyone)
			html += content_section_twentyone
		content_section_twentytwo = ""
		if page.content_section_twentytwo is not None:
			content_section_twentytwo = build_custom_template(request, page.content_section_twentytwo)
			html += content_section_twentytwo
		content_section_twentythree = ""
		if page.content_section_twentythree is not None:
			content_section_twentythree = build_custom_template(request, page.content_section_twentythree)
			html += content_section_twentythree
		content_section_twentyfour = ""
		if page.content_section_twentyfour is not None:
			content_section_twentyfour = build_custom_template(request, page.content_section_twentyfour)
			html += content_section_twentyfour
		content_section_twentyfive = ""
		if page.content_section_twentyfive is not None:
			content_section_twentyfive = build_custom_template(request, page.content_section_twentyfive)
			html += content_section_twentyfive
		content_section_twentysix = ""
		if page.content_section_twentysix is not None:
			content_section_twentysix = build_custom_template(request, page.content_section_twentysix)
			html += content_section_twentysix
		content_section_twentyseven = ""
		if page.content_section_twentyseven is not None:
			content_section_twentyseven = build_custom_template(request, page.content_section_twentyseven)
			html += content_section_twentyseven
		content_section_twentyeight = ""
		if page.content_section_twentyeight is not None:
			content_section_twentyeight = build_custom_template(request, page.content_section_twentyeight)
			html += content_section_twentyeight
		content_section_twentynine = ""
		if page.content_section_twentynine is not None:
			content_section_twentynine = build_custom_template(request, page.content_section_twentynine)
			html += content_section_twentynine
		content_section_thirty = ""
		if page.content_section_thirty is not None:
			content_section_thirty = build_custom_template(request, page.content_section_thirty)
			html += content_section_thirty
		# Use the page_template if the page_template is configured, otherwise
		# use the default.
		if page.page_template is not None:
			print("NOT NONE")
			template = Template(base64.b64decode(page.page_template.val).decode('utf-8'))
			print("TEMP")
			print(html)
			response = template.render(Context({
				"request": request,
				"leading_script": leading_script,
				"trailing_script": trailing_script,
				"leading_style": leading_style,
				"trailing_style": trailing_style,
				"aux_custom_template": aux_custom_template,
				"html": html,
				"page": "FOUND",
				"thing": "this is a thing",
				"content_section_one": content_section_one,
				"content_section_two": content_section_two,
				"content_section_three": content_section_three,
				"content_section_four": content_section_four,
				"content_section_five": content_section_five,
				"content_section_six": content_section_six,
				"content_section_seven": content_section_seven,
				"content_section_eight": content_section_eight,
				"content_section_nine": content_section_nine,
				"content_section_ten": content_section_ten,
				"content_section_eleven": content_section_eleven,
				"content_section_twelve": content_section_twelve,
				"content_section_thirteen": content_section_thirteen,
				"content_section_fourteen": content_section_fourteen,
				"content_section_fifteen": content_section_fifteen,
				"content_section_sixteen": content_section_sixteen,
				"content_section_seventeen": content_section_seventeen,
				"content_section_eighteen": content_section_eighteen,
				"content_section_nineteen": content_section_nineteen,
				"content_section_twenty": content_section_twenty,
				"content_section_twentyone": content_section_twentyone,
				"content_section_twentytwo": content_section_twentytwo,
				"content_section_twentythree": content_section_twentythree,
				"content_section_twentyfour": content_section_twentyfour,
				"content_section_twentyfive": content_section_twentyfive,
				"content_section_twentysix": content_section_twentysix,
				"content_section_twentyseven": content_section_twentyseven,
				"content_section_twentyeight": content_section_twentyeight,
				"content_section_twentynine": content_section_twentynine,
				"content_section_thirty": content_section_thirty,
			})).replace(" red"," #007bff")
			print(response)
			return HttpResponse(response)
		response = render_to_string("site_content/dynamic_page.html", {
			"request": request,
			"leading_script": leading_script,
			"trailing_script": trailing_script,
			"leading_style": leading_style,
			"trailing_style": trailing_style,
			"aux_custom_template": aux_custom_template,
			"html": html,
			"page": "FOUND",
			"thing": "this is a thing"
		}).replace(" red"," #007bff")
		return HttpResponse(response)
	except Exception as ex:
		print(str(ex))	
		return render(request, "site_content/dynamic_page.html", {
			"page": "404",
			"thing": "this is a thing"
		})

def fetchall_dict(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def build_custom_template(request, data):
	try:
		template = Template(base64.b64decode(data.template_data).decode('utf-8'))
		if data.sql_query == "":
			return template.render(Context({
				"request": request,
			}))	
		cursor = connection.cursor()
		cursor.execute(base64.b64decode(data.sql_query).decode('utf-8'))
		# https://www.postgresql.org/docs/9.5/functions-json.html
		rows = fetchall_dict(cursor)
		json_object_agg = None
		if data.result_type == "json_object_agg":
			json_object_agg = rows[0]["json_object_agg"]
		elif data.result_type == "json_array":
			rows = json.loads(rows)
		return template.render(Context({
			"request": request,
			"data": data,
			"rows": rows,
			"json_object_agg": json_object_agg, 
		}))	
	except Exception as ex:
		print(str(ex))
		msg_base = """
		<div class="container-fluid custom_template_error">
			<div class="row text-center">
				<div class="col-md-12">
				Oops... there was an problem loading this section.	
				</div>
			</div>
			<div class="row text-center">
				<div class="col-md-12" %s>
					<br>
					<code>
						%s
					</code>
				</div>
			</div>
			<div class="row text-left">
				<div class="col-md-12" %s>
					<code style='color: white; background: #ffffff00;'>
						%s
					</code>
				</div>
			</div>
		</div>
		"""
		if settings.ENV == "production":
			return msg_base % (
				"style='display: none;'","",
				"style='display: none;'",""
			)
		backtrace = traceback.format_exc()
		backtrace = backtrace.replace("\n","<br />\n")
		backtrace = backtrace.replace("  ","&nbsp;&nbsp;&nbsp;")
		return msg_base % (
			"", str(ex),
			"", backtrace
		)

def blog_home(request):
	carousel_items = CarouselRow.objects.all()
	return render(request, "site_content/home_page.html", {
		"name": "blog_home",
		"thing": "this is a thing",
		"carousel_items": carousel_items 
	})

def blog(request, page="default"):
	carousel_items = CarouselRow.objects.all()
	return render(request, "site_content/home_page.html", {
		"name": "blog" + page,
		"thing": "this is a thing",
		"carousel_items": carousel_items 
	})
