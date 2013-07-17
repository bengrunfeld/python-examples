#! /usr/bin/python


pageWidth=1080		#Input the page width
numberOfCols=30		#Input how many colums you want
margin=30			#Input how much space you think is good

if((pageWidth-(margin * (numberOfCols - 1))) % numberOfCols) == 0:
	cols = (pageWidth-(margin*(numberOfCols-1)))/numberOfCols
	print "Column Width should equal:", cols
else:
	print "Sorry, that won't work."