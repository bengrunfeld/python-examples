#! /usr/bin/python

def shopping_list(item, *questions, **actors):
	print "I need some", item
	print "Sure, we've got a nice big bunch of", item
	for q in questions:
		print q
	print "*" * 50
	print "/" * 50
	acts = sorted(actors.keys())
	for a in acts:
		print a, ":", actors[a]

shopping_list("eggs", 
			  "Are they fresh?", 
			  "They don't smell so fresh...", 
			  customer='Natalie Portman',
			  vendor='Musty Eggs',
			  attendant='Ron Jeremy')