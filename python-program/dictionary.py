dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'

#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 15; # update existing entry
dict['School'] = "Bloomig dales modern public school"; # Add new entry

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']