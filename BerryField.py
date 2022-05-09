# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:11:22 2022

@author: Philip Paterson
HW 8 BerryField Class
This is the class for the berry field, which hosts berries, bears, and 
tourists.
"""

class BerryField(object):
    """This is the berry field class, which hosts berries, bears, and 
    tourists.
    """
    
    def __init__(
            self, 
            grid, 
            active_bears= [], 
            reserve_bears= [],
            active_tourists= [],
            reserve_tourists= []
            ):
        
        self.field = grid
        self.active_bears = active_bears
        self.reserve_bears = reserve_bears
        self.gone_bears = []
        self.active_tourists = active_tourists
        self.reserve_tourists = reserve_tourists
        self.gone_tourists = []
        self.total_berries = sum(list(map(lambda r: sum(r), self.field)))
    
    
    def check_bear_here(self, r, c):
        """Checks if there is a bear at the given location

        Args:
            r (INT): The row number
            c (INT): The column number

        Returns:
            BOOL: Whether or not the bear is at the given location
        """
        i = 0
        while i < len(self.active_bears): 
            if self.active_bears[i].row == r and self.active_bears[i].column == c:
                return True
            else:
                i += 1
        return False
    
    
    def check_tourist_here(self, r, c):
        """Checks if there is a tourist at the given location

        Args:
            r (INT): The row number
            c (INT): The column number

        Returns:
            BOOL: Whether or not the tourist is at the given location
        """
        j = 0
        while j < len(self.active_tourists): 
            if self.active_tourists[j].row == r and self.active_tourists[j].column == c:
                return True
            else:
                j += 1
        return False
    
    
    def retire_bears(self):
        """This function retires the active bears to the reserve bears.
        """
        for b in self.gone_bears:
            if b in self.active_bears:
                self.active_bears.remove(b)
                

    def retire_tourists(self):
        """This function retires the active bears to the reserve bears.
        """
        for t in self.gone_tourists:
            if t in self.active_tourists:
                self.active_tourists.remove(t)
    
    
    def __str__(self):
        """Formats the BerryField data to a string.

        Returns:
            STR: BerryField data.
        """
        # Formatting the field grid
        field_string = ''
        r = 0
        while r < len(self.field):
            c = 0
            while c < len(self.field[r]):
                # Determining what the output should be for the location
                bear_here = self.check_bear_here(r, c)
                tourist_here = self.check_tourist_here(r, c)
                if bear_here and tourist_here:
                    out = 'X'
                elif bear_here:
                    out = 'B'
                elif tourist_here:
                    out = 'T'
                else:
                    out = self.field[r][c]
                
                field_string += "{:>4}".format(out)
                c += 1
            field_string += '\n'
            r += 1
        self.total_berries = sum(list(map(lambda r: sum(r), self.field)))
        total_berries_string = 'Field has {0} berries.\n'.format(self.total_berries)
        
        # Formatting state of active bears
        active_bears_string = '\nActive Bears:\n'
        for b in self.active_bears:
            active_bears_string += str(b) + '\n'

        # Formatting state of active tourists
        active_tourists_string = '\nActive Tourists:'
        for t in self.active_tourists:
            active_tourists_string += '\n' + str(t)

        # Formatting the total string of the state of the berry field
        field_state = total_berries_string + field_string + \
            active_bears_string + active_tourists_string
        
        return field_state
        
        
    def grow(self):
        """This function grows the berry bushes on the berry field.
        """
        # Grow individual berry bush location
        r = 0
        while r < len(self.field):
            
            c = 0
            while c < len(self.field[r]):
                if self.field[r][c] >= 1 and self.field[r][c] < 10:
                    self.field[r][c] += 1
                c += 1
            r += 1
        # Spreads berries from adjacent berry bushes
        r = 0
        while r < len(self.field):
            c = 0
            while c < len(self.field[r]):
                ten_berries_near = False
                if self.field[r][c] == 0:
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if r + dr >= 0 and r + dr < len(self.field) \
                                and c + dc >= 0 and c + dc < len(self.field) \
                                and self.field[r + dr][c + dc] == 10:
                                    ten_berries_near = True
                if ten_berries_near:
                    self.field[r][c] += 1
                c += 1
            r += 1
        self.total_berries = sum(list(map(lambda r: sum(r), self.field)))