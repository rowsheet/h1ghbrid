#!/usr/bin/env python
import os
import sys
"""
Note:

This file has been modifed to include Adilas cron job scripts. On startup of Django,
this file will run, which should also run the adilas.py CRON_INIT() function.
CRON_INIT will start a background thread. This background thread will repeatidly run
CRON_JOB, then slepp every CRON_MINUTES.
"""
import adilas_cron
import threading

if __name__ == "__main__":
	"""
	NOTE: 
	Uncomment bellow to initialize cron job; specify the hours.
	"""
	# Initialize adilas cron tasks here.
	"""
	hours = 12
	seconds = hours * 60
	adilas_cron_job_thread = threading.Thread(target=adilas_cron.CRON_JOB, kwargs={"seconds": seconds})
	adilas_cron_job_thread.start()
	"""

	# Do normal Django startup things.
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
