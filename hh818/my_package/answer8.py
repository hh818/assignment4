'''
Created on Feb 27, 2015

@author: ds-ga-1007
'''
#create dictionary di
di = {'first':[2,1], 'second':[2,3], 'third':[3,4]}

#duplicate di2 = di
di2 = di.copy()

#a. swap the values of the first and third keys
di['first'] = di2['third']
di['third'] = di2['first']

#b. Sort the elements of the list with key third
di['third'].sort()

#c.Add a new key fourth with the value of the key second
di['fourth'] = di['second']

#d. Delete the key/value pair second
del di['second']

#print out di
print di
