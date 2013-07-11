#! /usr/bin/python

names = ['b', 'e', 'n', 'n', 'n', 'n', 'y']

for i in range(len(names)):
        if names[i] == 'n':
                continue
	else:
		print i, names[i]

else:
        print "End of the name"
