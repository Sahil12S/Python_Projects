# Project: Website blocker
# Author: Sahil Sharma
# Created on: 02/09/2018
# Last edited: 02/09/2018


import time
from datetime import datetime as dt

hosts_temp = "hosts"

# Initialize a variable to hold path of hosts file.
# hosts file will store websites that we are planning to block.
hosts_path = "/etc/hosts"

# IP address where browser will be redirected. In this case it is localhost.
redirect = "127.0.0.1"

# List of websites that we want to block.
website_list = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 13) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			# Loop to add website in host file if it doesn't exist.
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		print("Fun time...")
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			# print(content)
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(10)
