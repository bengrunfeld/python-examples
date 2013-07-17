#! /usr/bin/python

def shopping_list(*questions):
	for q in questions:
		print q
	print "*" * 50

shopping_list(12, 
			  "Are they fresh?", 
			  "They don't smell so fresh...",
			  "Sorry, my eggs are a bit off", 
			  "Oh, I'm gonna puke")