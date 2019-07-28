"""
filter(**kwargs)
exclude(**kwargs)
# annotate()
order_by()
reverse()
distinct()
values()
values_list()
dates()
datetimes()
none()
all()
union()
intersection()
difference()
select_related()
prefetch_related()
extra()
defer()
only()
using()
select_for_update()
raw()
"""
import re

def call_dynamic(app, klass, method, args = None):
	path = app + ".models"
	module = __import__(path, fromlist=[klass])
	obj = getattr(module, klass)
	return getattr(obj, method)(args)

def b64encode(data):
	return = base64.b64encode (bytes('data to be encoded', "utf-8"))

def log_malicous(info):
	print("TODO: log")

def debug(obj):
	"-----------DEBUG: " + obj + " --------------"

"""
Return an object assuming it's in the "models.py" file of some module in the root 
directory of the Django app.

Path should have a naming contention like:
	"cms.Page"
Where the string portions are:
	"module.Class"
"""
def load_object(path):
	try:
		app = path.split(".")[0]
		klass = path.split(".")[1]
		# Clean paths for security.
		app_clean = re.sub('[^0-9a-zA-Z]+', '', app)
		klass_clean = re.sub('[^0-9a-zA-Z]+', '', klass)
		# @TODO @TODOPROD log potential malicous requests.
		if app_clean != app:
			log_malicous({
				"original": app,
				"claan": app_clean
			})
		if klass_clean != klass:
			log_malicous({
				"original": klass,
				"clean": klass_clean
			})
		# Assume the object is in the models file.
		model_path = app + ".models"
		# Import the module.
		module = __import__(model_path, fromlist=[klass])
		# Import the object.
		obj = getattr(module, klass)
		# Return the object.
		return obj
	except Exception as ex:
		print(str(ex))
		msg = "Unable to parse object path: '" + path + "'."
		raise Exception(msg)

def parse_args(args):
	try:
		# Parse the object from JSON.
		if args is None:
			return None
		if type(args) == list:
			return args
	except Exception as ex:
		print(str(ex))
		msg = "Invalid arguments."
		raise Exception(msg)

"""
Configure API access.

"""
config = {
	"default_methods": {
		"order_by",		
		"reverse",
		"filter",
	},
	"object_config": {
		"cms": {
			"ContentSection": {
			},
			"CustomCSS",
			"CustomJS",
			"PageTemplate",
			"Page",
			"TextBit",
		},
		"storefront": {
			"Product": {}
		}
	}
}

"""
Processes and validates a JSON decoded request dictionary with keys:
1) obj (must be cleaned)
2) method (must be one-word and validated)
3) args (optional)
"""
def process_request(data):

if __name__ == "__main__":
	import cli
	"""
	page = load_object("cms.Page")
	# page = load_object(".Page")
	print(page)
	"""
	# Method with no parameters.
	data = {
		"obj": "cms.Page",
		"method": "all"
	}
	"""
	# Method with *args parameters.
	obj = "cms.Page"
	method = "order_by"
	args = '["title", "creation_timestamp"]'

	# Method with **kwargs parameters.
	obj = "cms.Page"
	method = "create"
	args = 
		{"title": "TEST",
		"page_title": {
			"cms.PageTemplate": {
				"key": "base"
			}
		}
	"""
