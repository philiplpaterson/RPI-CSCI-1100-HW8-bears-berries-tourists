# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:37:43 2022

@author: Philip Paterson
HW 8 Part 1
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
    
    print()
    print(berry_field)