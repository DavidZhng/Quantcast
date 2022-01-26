#!/usr/bin/env python3

import sys
import csv
import argparse

def main(args):
	#Parse args
	parser = argparse.ArgumentParser(description='Most active cookie')
	parser.add_argument('filename', type=str, help='Input filename')
	parser.add_argument('-d', dest='date', type=str, help='Query date', required=True)
	args = parser.parse_args(args)

	#Check input file is .csv
	if args.filename[-4:] != '.csv':
		print("Must use a csv file", file=sys.stderr)
		sys.exit(1)

	#Dictionary that maps cookies to occurents on args.date
	cookie_counts = dict()

	with open(args.filename, newline='') as csvfile:
	    csvreader = csv.reader(csvfile)
	    for row in csvreader:
	    	#Check if day of active cookie matches args.date
	        if row[1][:10] == args.date:
	        	if row[0] in cookie_counts:
	        		cookie_counts[row[0]] += 1
	        	else:
	        		cookie_counts[row[0]] = 1
	        #End the loop since all cookies on args.date have been seen
	       	elif row[1][:10] != args.date and cookie_counts:
	       		break
	# Exit program if no cookies on args.date
	if not cookie_counts:
		sys.exit(3)
	# Maximum number of occurences of a single cookie on args.date
	max_count = max(cookie_counts.values())
	#Print all the keys of max occurence
	for key in cookie_counts:
		if cookie_counts[key] == max_count:
			print(key)

if __name__ == "__main__":
	main(sys.argv[1:])