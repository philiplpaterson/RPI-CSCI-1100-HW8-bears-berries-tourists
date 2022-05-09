# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:13:40 2022

@author: Philip Paterson
HW 8 Part 3
This program runs a simulation of a berry field containing berries, bears, and
tourists. The bears can eat berries that grow in the field and they can eat
tourists that watch for the bears. The program ends when there are no more
bears in the field and no more bears in the reserve list.
"""

import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

# Main body of the Code
if __name__ == "__main__":
    '''
    json files to test:
        bears_and_berries_1.json
        bears_and_berries_2.json
    '''
    fname = input("Enter the json file name for the simulation => ").strip()
    print(fname)
    
    f = open(fname)
    data = json.loads(f.read())

    # Creating the objects
    act_b = list(map(lambda b: Bear(b[0], b[1], b[2]), data["active_bears"]))
    res_b = list(map(lambda b: Bear(b[0], b[1], b[2]), data["reserve_bears"]))
    act_t = list(map(lambda t: Tourist(t[0], t[1]), data["active_tourists"]))
    res_t = list(map(lambda t: Tourist(t[0], t[1]), data["reserve_tourists"]))
    berry_field = BerryField(data["berry_field"], act_b, res_b, act_t, res_t)
    
    print("\nStarting Configuration")
    print(berry_field)
    turn = 1
    
    # Defining the stop condition
    cond_stop = (len(berry_field.active_bears) == 0 and \
                 len(berry_field.reserve_bears) == 0) \
        or (len(berry_field.active_bears) == 0 and \
            berry_field.total_berries <= 0)
    
    # Main loop
    while not cond_stop:
        # Growing the berry field
        berry_field.grow()
        
        # Moving the bears
        for b in berry_field.active_bears:
            b.move(berry_field)   
        berry_field.retire_bears()
        
        # Checking on the tourists
        for t in berry_field.active_tourists:
            t.check_bear(berry_field)      
        berry_field.retire_tourists()
        
        # Printing if mammals left
        print("\nTurn:", turn)
        for b in berry_field.gone_bears:
            if not b.announced:
                print(b)
                b.announced = True
        for t in berry_field.gone_tourists:
            if not t.announced:
                print(t)
                t.announced = True
        
        # Adding reserve bears
        if len(berry_field.reserve_bears) > 0 and berry_field.total_berries >= 500:
            berry_field.active_bears.append(berry_field.reserve_bears.pop(0))
            print(berry_field.active_bears[-1], "- Entered the Field")
            bear_added = True
        else:
            bear_added = False
            
        # Adding Reserve Tourists
        if len(berry_field.reserve_tourists) > 0 and len(berry_field.active_bears) >= 1:
            berry_field.active_tourists.append(berry_field.reserve_tourists.pop(0))
            print(berry_field.active_tourists[-1], "- Entered the Field")
            tourist_added = True
        else:
            tourist_added = False
        
        # Checking if the program should stop
        if (len(berry_field.active_bears) == 0 and \
                     len(berry_field.reserve_bears) == 0) \
            or (len(berry_field.active_bears) == 0 and \
                berry_field.total_berries <= 0):
                cond_stop = True
        
        # Printing the status of the field every 5 turns, or when program stops
        if turn % 5 == 0:
            print(berry_field)
            print()
        elif cond_stop:
            print()
            print(berry_field)
        else:
            print()
        turn += 1