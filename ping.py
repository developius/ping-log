#!/usr/bin/python

import subprocess
import time
import datetime
import sys

urls = [
	["bbc", "212.58.244.66"],
	["router", "192.168.1.254"]
]
subprocess.call("rm results/" + sys.argv[1] + ".csv", shell=True)

print("Writing to results/" + sys.argv[1] + ".csv")
started = time.time()

while True:
	if time.time() - started < 60:
		with open("results/" + sys.argv[1] + ".csv", "a") as theFile:
			for url in urls:
				p = subprocess.Popen(['ping','-c','1', url[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				out, err = p.communicate()

				out = out.split("\n")[1].split("time=")[-1]
				out = str(datetime.datetime.now()) + "," + url[0] + "," + out
				theFile.write(out + "\n")

				out = out.split(",")
				print("[" + out[0] + "] " + out[1] + ":\t" + out[2])
		theFile.close()
		time.sleep(0.5)

	else:
		print("Complete")
		break
