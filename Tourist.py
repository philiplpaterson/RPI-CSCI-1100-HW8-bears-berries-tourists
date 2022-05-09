# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:33:15 2022

@author: Philip Paterson
HW 8 Tourist Class
The tourist class defines a tourist in the berry field that stays still and
watches for bears
"""
import math

class Tourist(object):
    
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.bears_seen = 0
        self.turns_no_bears = 0
        self.gone = False
        self.announced = False
    
    
    def __str__(self):
        """Formats tourist data to a string.

        Returns:
            STR: Tourist data.
        """
        tourist_string = "Tourist at ({0},{1}), {2} turns without seeing a bear.".format(
            self.row,
            self.column,
            self.turns_no_bears
            )
        
        if self.gone:
            tourist_string += " - Left the Field"
        
        return tourist_string
    

    def check_bear(self, b_field):
        """Checks if there is a bear either at the tourist's location, or at or
        within 4 units of it.

        Args:
            b_field (BerryField): The berry field object.
        """
        # Checking if a bear is at the tourist's position
        if b_field.check_bear_here(self.row, self.column):
            self.gone = True
        else:
            self.bears_seen = 0
            # Seeing if a bear is within 4 units
            for b in b_field.active_bears:
                distance = ((b.row - self.row)**2 + (b.column - self.column)**2)**0.5
                if math.isclose(distance, 4.0) or distance < 4.0:
                    self.bears_seen += 1
            # Checking if any bears have been seen
            if self.bears_seen <= 0:
                self.turns_no_bears += 1
            else:
                # Resetting the numer of turns with no bears seen
                self.turns_no_bears = 0
            # Checking if it has been 3 or more turns without seeing a bear
            if self.turns_no_bears >= 3:
                self.gone = True
            else:
                if self.bears_seen >= 3:
                    self.gone = True
        # Adds tourist to the b_field.gone_tourists list.
        if self.gone:
            b_field.gone_tourists.append(self)
            return