#! /usr/bin/python

#Program Description: You input the page width you're dealing with,
#how many columns you'd like to create, and what the space should 
#be between the columns, and the program calculates if you can create
#columns of equal width. If you can't, it issues an error message.


pageWidth=1080		#Input the page width
numberOfCols=3		#Input how many colums you want
margin=30			#Input how much space you think is good

if((pageWidth-(margin * (numberOfCols - 1))) % numberOfCols) == 0:
	cols = (pageWidth-(margin*(numberOfCols-1)))/numberOfCols
	print "Column Width should equal:", cols
else:
	print "Sorry, that won't work."