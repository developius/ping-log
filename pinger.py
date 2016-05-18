#!/usr/bin/python

# usage:
# pinger <results file name> <seconds to run for> <gap between pings>

# script to set off a ping to two specified hosts:
# www.google.co.uk (should be reliable?)
# your router
# records round trip ms to a csv file in specified filename in 'results' folder

# code: @developius, @dataknut


import subprocess
import time
import datetime
import sys


# how long to run for in minutes?
duration = float(sys.argv[2])
# gap between pings (seconds)
gap = float(sys.argv[3])


print("Running for " + str(duration) + " minutes")
print("Gap between pings: " + str(gap) + " second/s")

urls = [
	["www.google.co.uk", "www.google.co.uk"], # 74.125.136.94
	["router", "192.168.1.254"]
]

# record start time to use as part of the results filename
startdt = datetime.datetime.now().strftime(format = "%Y-%m-%d_%H-%M-%S")

ofile = "results/" + sys.argv[1] + "_" + startdt + ".csv"

print("Writing to: " + ofile)

started = time.time()

with open(ofile, "a") as theFile:
	# print header
	theFile.write("timestamp,host,milliseconds,error" + "\n")
theFile.close()

while True:
	if time.time() - (started) < duration*60: # check how long we've been running against specified duration which is in minutes
		with open(ofile, "a") as theFile:
			for url in urls:
				now = datetime.datetime.now().strftime(format = "%Y-%m-%d %H:%M:%S")
				p = subprocess.Popen(['ping','-c','1', url[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				out, err = p.communicate()
				try:
					ms = out.split("\n")[1].split("time=")[-1].split(" ")[0]	
					# set a nice datetime for R etc	
					# allow for error column at the end																																																																				
					out =  now + "," + url[0] + "," + ms + "," + "OK"
				except IndexError:
					# Error in indexing the split list from ping
					# Probably no internet connection at all so ping has failed
					# set the error message to be output
					# need to remove \n from the end of the error string
					error = ("%s" % err)
					# set a nice datetime for R etc
					# leave ms empty & add error
					out = now + "," + url[0] + "," + "," + error.split("\n")[0]
				# there are a load of other ping error responses we really ought to catch properly
				theFile.write(out + "\n")

				out = out.split(",")
				print("[" + out[0] + "] " + out[1] + ": " + out[2] + ": " + out[3])
		theFile.close()
		time.sleep(gap)

	else:
		print("Complete")
		break
