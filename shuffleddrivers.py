# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:21:37 2017

@author: jub061
"""

from random import shuffle

drivers = {'A' : 'Bruce', 'B' : 'Nick'}
direction = {'E' : "East", 'W' : "West"}
speed = {'F':55 , 'S' : 30}
replicates = range(2)
testCombos = [(driver, direct, sp, rep) for driver in drivers for direct in direction for sp in speed for rep in replicates]

print('Ordered Test Combinations:')
print(testCombos)

shuffle(testCombos)
print('Shuffled Test Combinations')
print('Code\t\t\tDriver\tDirection\tSpeed (mph)\tReplicate')
for t in testCombos:
    print(t, end='\t')
    print(drivers[t[0]], end='\t')
    print(direction[t[1]], end='\t\t')
    print(speed[t[2]], end='\t\t')
    print(replicates[t[3]])