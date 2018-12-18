import time
import json
from datetime import datetime
import os.path


root = '/home/ubuntu/asset'
day = str("%02d" % datetime.now().day)+"-"+str("%02d" % datetime.now().month)+"-"+str("%04d" % datetime.now().year)
f2 = os.path.join(root,domain,day,'report')

def touch(filename):
	fname = filename
	file = open(fname, 'w')
	file.close()

def export(domain, report, _type, fields=False):
	timestamp = time.time()
	filename = f2+'.'+_type
	if _type == 'csv':
		csv_report = ''
		if fields:
			csv_report += 'ip,status,type,domain_name,server,http_headers\n'
		for item in report:
			csv_report += item + '\n'
		report = csv_report
	try:
		with open(filename, 'a') as f:
			f.write(report)
		f.close()
		return '\n'+_type.upper()+' report saved in: '+filename
	except: 
		return '\nCannot write report file: '+filename
