#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from datetime import date
import dss #service
import dps #part
import dsoh #stock

def rebuildXML(filename, parser, backupfolder):
	output = None
	try:
		service = parser.parse("Input/%s" % filename)
		output = open("Output/%s" % filename, "w")
		service.export(output, 0)
	except Exception as e:
		print "[ERROR] %s failed!" % filename
		print(e)
		return False
	else:
		os.rename("Input/%s" % filename, "%s/%s" % (backupfolder, filename))
		print "%s corrected." % filename
		return True
	finally:
		if output is not None:
			output.close()

def run():
	files = os.listdir("Input")
	backupfolder = date.today().strftime('%Y%m%d')
	try:
		os.stat(backupfolder)
	except:
		os.mkdir(backupfolder)

	for filename in files:
		parser = None
		if filename.lower().endswith("serv.xml"):
			parser = dss
		elif filename.lower().endswith("stock.xml"):
			#parser = dsoh
			pass
		elif filename.lower().endswith("part.xml"):
			#parser = dps
			pass
		else:
			print "%s unknown type." % filename
		if parser is not None:
			rebuildXML(filename, parser, backupfolder)
		else:
			print "%s skipped." % filename

USAGE_TEXT = """
Usage: python <Rebuild>.py [-h|--help]
"""

def usage():
	print(USAGE_TEXT)
	sys.exit(1)

def main():
	args = sys.argv[1:]
	print "System encoding is [%s]" % sys.getdefaultencoding()
	if len(args) > 0 and (args[0] == "-h" or args[0] == "--help"):
		usage()
	else:
		run()

if __name__ == '__main__':
	main()


