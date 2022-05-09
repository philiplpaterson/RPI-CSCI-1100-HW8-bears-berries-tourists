# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:25:32 2022

@author: Philip Paterson
HW 8 Part 2
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
    while turn <= 5:
        # Growing the berry field
        berry_field.grow()
        
        # Moving the bears
        for b in berry_field.active_bears:
            b.move(berry_field)
            
        # Checking on the tourists
        for t in berry_field.active_tourists:
            t.check_bear(berry_field)
        
        berry_field.retire_bears()
        berry_field.retire_tourists()
        
        print("\nTurn:", turn)
        for b in berry_field.gone_bears:
            if not b.announced:
                print(b)
                b.announced = True
        for t in berry_field.gone_tourists:
            if not t.announced:
                print(t)
                t.announced = True
        print(berry_field)
        print()
        turn += 1