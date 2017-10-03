# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:05:07 2017

@author: jub061
"""
import random
from random import shuffle

right_1st = 0
right_2nd = 0
end_range = 100
for iterate in range(0, end_range):
    #setup
    doors = [0, 0, 1]
    options = [0, 1, 2]
    shuffle(doors)
    print('doors are', doors)
    
    #isolate the 0 doors
    one = doors.index(1)
    zero_1 = doors.index(0)
    diff_door = doors
    diff_door[zero_1] = 1
    zero_2 = diff_door.index(0)
    zeros = [zero_1, zero_2]
    print('zeros', zeros)
    print('one', one)
    
    #pick a door at random
    pick = random.choice(options)
    print("1st choice is", pick)
    
    # "open a door"
    if pick == zeros[0]:
        opend = zeros[1]
        print('pick was:', zeros[0], ' so opened:', zeros[1])
        
    elif pick == zeros[1]:
        opend = zeros[0]
        print('pick was:', zeros[1], ' so opened:', zeros[0])    
    else:   
        opend = random.choice(zeros)
        print('pick was:', pick, ' so opened:', opend)
            
   
    #print('open door is:',opend)
    #pick a new door
    not_picked =[opend, pick]
    #print('not picked', not_picked)

    for i in sorted(not_picked, reverse=True):
        del options[i]
    
    pick2 = options[0]
    print("second pick is:", pick2)
    

    if pick == one:
        right_1st +=1
    
    if pick2 == one:
        right_2nd +=1
        
        
print('first choice was right ', right_1st, 'out of ', end_range)        
print('second choice was right ', right_2nd, 'out of ', end_range)