#! /usr/bin/python

def shout(times, message="You're stinky", volume=100):
	print message * times
	print "at a volume of", volume

args = {"times": 5, "message": "Please take a shower sir \n", "volume": "50"}
shout(**args)

