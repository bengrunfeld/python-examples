#! /usr/bin/python
names = ['b', 'e', 'n', 'n', 'n', 'n', 'y']
for i in range(len(names)):
        if i == 'n':
                continue
	elif i != 'n':
		print i, names[i]

else:
        print "End of the name"
