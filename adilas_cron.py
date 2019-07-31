"""-----------------------------------------------------------------------------
NOTE: THIS FILE IS STILL IN TEST MODE!
-----------------------------------------------------------------------------"""

"""
ADALAS IMPORT TASK FILE.

This file should be run on the startup of Django (when manage.py is run) in a
separate thread.
"""
import psycopg2
import urllib.parse
import os
import threading
import datetime
import time
import json
import requests
from django.http import HttpResponse

def sync_products_button(request, page="home"):
	try:
		UPDATE_FROM_ADILAS()
		return HttpResponse("Update complete", status=200)
	except Exception as ex:
		return HttpResponse(str(ex), status=500)

# Some things are encoded multiple times.
# Also remove all single quotes.
def unescape(msg):
	return urllib.parse.unquote(
		urllib.parse.unquote(
			urllib.parse.unquote(
				urllib.parse.unquote(
					msg.replace("'","")
				)
			)
		)
	)

def fetch_products():
	print("Fetching products...")
	arr = []
	for i in range(1,4):
		d = {
			"API_CALL_FUNCTION_NAME": "getWebGeneralInventory",
			"API_CORP_KEY_ID": "THE-0410",
			"API_CURRENT_PAYEE_ID": 71300,
			"API_INPUT_OUTPUT_TYPE": "JSON",
			"API_URL_ENCODING": "AUTO",
			"API_USER_NAME": "metrcTensor",
			"API_USER_PASSWORD": "selectAdilas$",
			"CORP_KEY_ID": "THE-0410",
			"PAGE_NUMBER": i,
			"PART_CATEGORY_ID": "All",
			"PART_NUMBER": "All",
			"SHOW_PER_PAGE": 1000,
			"SHOW_UNLIMITED": True,
		}
		ds = "call_function_data=" + urllib.parse.quote(json.dumps(d, separators=(",",":"))) + "&submit_btn=Run+It"
		r = requests.post("https://www.adilas.biz/web/adilas_api_calls.cfm",
			headers = {
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "en-US,en;q=0.9",
				"Cache-Control": "max-age=0",
				"Connection": "keep-alive",
				"Content-Length": str(len(ds)),
				"Content-Type": "application/x-www-form-urlencoded",
				"Cookie": "PHPSESSID=gc5ehu7cvqnrv705eo7p8v33uh; CFID=7984477; CFTOKEN=4418e7170e54d598-83185836-E864-519D-3CB84061E00301DF",
				"Host": "www.adilas.biz",
				"Origin": "https://www.adilas.biz",
				"Referer": "https://www.adilas.biz/web/show_adilas_api_calls.cfm",
				"Upgrade-Insecure-Requests": "1",
				"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
			},
			data = ds
			)
		arr += json.loads(r.text)['QRY_GENERAL_INVENTORY_ARRAY']
	return arr

# Test with 374989
def update_product(product, job_timestamp):
	# We at least need to PARTID, otherwise we can't even log the product
	# as an import error if it occurrs. Don't even try if it's not there.
	if "PARTID" not in product:
		# @TODO log this somewhere.
		print("Recieved product with no known UPC or PARTID.")
		return
	print("Updating product: '%s'" % product["PARTID"])
	try:
		con = psycopg2.connect(os.environ.get("DATABASE_URL"))
		cur = con.cursor()
		sql = """
		INSERT INTO storefront_product
		(
			visible,
			for_sale,
			discontinued,
			vendor,
			inventory,

			uofm,
			description,
			price,
			base_price,
			vendor_code,
			name,
			category,
			adilas_import_timestamp,
			adilas_active,
			adilas_import_error
		) VALUES (
			False,
			False,
			False,
			'Unknown',
			0,

			'%s',
			'%s',
			'%f',
			'%f',
			'%s',
			'%s',
			'%s',
			'%s',
			False,
			False
		) ON CONFLICT (upc)
		DO UPDATE SET
			uofm = '%s',
			description = '%s',
			price = '%f',
			base_price = '%f',
			vendor_code = '%s',
			name = '%s',
			category = '%s',
			adilas_import_timestamp = '%s',
			adilas_active = True,
			adilas_import_error = False,
			upc = '%s'	
		""" % (
			unescape(product["UOMINITIALS"]),
			unescape(product["PARTDESCRIPTION"]),
			product["PARTSALEPRICE"],
			product["PARTCOST"],
			str(product["VENDORPAYEEID"]),
			unescape(product["PARTNUMBER"]),
			unescape(product["PARTCATEGORYNAME"]),
			job_timestamp,
			unescape(product["UOMINITIALS"]),
			unescape(product["PARTDESCRIPTION"]),
			product["PARTSALEPRICE"],
			product["PARTCOST"],
			str(product["VENDORPAYEEID"]),
			unescape(product["PARTNUMBER"]),
			unescape(product["PARTCATEGORYNAME"]),
			job_timestamp,
			str(product["PARTID"]),
		)
		cur.execute(sql)
		con.commit()
	except Exception as ex:
		print(str(ex))
		con = psycopg2.connect(os.environ.get("DATABASE_URL"))
		cur = con.cursor()
		sql = """
		UPDATE
			storefront_product
		SET
			adilas_active = False,
			adilas_import_timestamp = '%s',
			adilas_import_error = True 
		WHERE
			upc = '%s'	
		""" % (
			job_timestamp,
			str(product["PARTID"])
		)
		cur.execute(sql)
		con.commit()

# Pull adilas data.
def UPDATE_FROM_ADILAS():
	print("Running adilas update...")
	job_timestamp = datetime.datetime.now()
	products = fetch_products()
	for product in products:
		update_product(product, job_timestamp)	

# This job runs another job in a continous loop with a specified amount of seconds.
# This should be run in a new thread.
def CRON_JOB(**kwargs):
	print("Initializing CRON_JOB.")

	# Seconds have to be defined so we know how long to sleep.
	if "seconds" not in kwargs:
		raise Exception("Invalid CRON_JOB, seconds not defined.")

	# The job has to run continously. This should be run in a new thread.
	while(True):
		# Run the actual update procedure.
		UPDATE_FROM_ADILAS()
		# Sleep for however long specified.
		time.sleep(kwargs["seconds"])

"""
Unit test CRON_JOB.

This will only be run if this file alone is run from the CLI (command line interface), thus
this also serves as the unit test for this file.

Run:
	$ python3 adalis.py
"""
if __name__ == "__main__":
	print("Starting adilas.py CHRON_JOB unit test...")
	# Unit test CRON_JOB in the thread.
	"""
	# Initialize adilas cron tasks here.
	adilas_cron_job_thread = threading.Thread(target=CRON_JOB, kwargs={"seconds": 3})
	adilas_cron_job_thread.start()
	print("AFTER THREAD START...")
	"""
	# Unit test UPDATE_FROM_ADILAS.
	UPDATE_FROM_ADILAS()
