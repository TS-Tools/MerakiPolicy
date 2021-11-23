import argparse
import calendar
import time
import sys
import os
import subprocess

if __name__=='__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument("--var1", "-v1", help="What we're searching for")

	args = parser.parse_args()

	if args.var1:
		#output=open("output.txt","a",encoding="utf-8",newline='')
		output = open("output.txt", "a")
		status="Not Found / Implicit Permit"
		with open("MerakiConfig.txt","r") as lines:
			for line in lines:
				if args.var1 in line.strip():
					policy=line.strip().split('"policy":')[1].split(",")[0].replace('"',"")
					if policy.lower()=="deny":
						status="Blocked"
						break
					else:
						status="Permitted"
						break
		timestamp = calendar.timegm(time.gmtime())
		#f.write("$Meraki L3 Rules - "+args.var1+" - ["+status+"] "+"\n")
		output.write("$Meraki L3 Rules - "+status+"\n")  #" - ["+args.var1+"] "+"\n")
		#f.write("$Meraki L3 Rules - "+status"+"\n")		

	else:
		print("No searchable variable received")
		

