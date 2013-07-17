#! /usr/bin/python

def shopping_list(**questions):
	qs = sorted(questions.keys())
	for q in qs:
		print q, ":", questions[q]

shopping_list(eggs=12, 
			  question="Are they fresh?", 
			  nextQuestion="They don't smell so fresh...",
			  answer="Sorry, my eggs are a bit off", 
			  nextAnswer="Oh, I'm gonna puke")
