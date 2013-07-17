#! /usr/bin/python

"""Calculates how wide floating columns should be in a set page width.

You input the page width you're dealing with, how many columns you'd 
like to create, and what the space should be between the columns, and 
the program calculates if you can create columns of equal width and 
what that width should be. If you can't create colums of equal width, 
it issues an error message."""


pageWidth=930		#Input the page width
numberOfCols=4		#Input how many colums you want
margin=30		#Input how much space you think is good

if((pageWidth-(margin * (numberOfCols - 1))) % numberOfCols) == 0:
	cols = (pageWidth-(margin*(numberOfCols-1)))/numberOfCols
	print "For a page width of:", pageWidth, "pixels,"
	print "With", numberOfCols, "columns,"
	print "Column Width should be:", cols, "pixels,"
	print "With", margin, "pixels margin in between them."
else:
	print "Sorry, that won't work."
