# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:31:49 2022

@author: Philip Paterson
HW 8 Bear Class
The bear class defines a Bear, which eats berries, eats tourists, and moves.
"""

class Bear(object):
    """The bear class defines a Bear, which eats berries, eats tourists, and 
    moves.
    """

    def __init__(self, row, column, direction):
        self.row = row
        self.column = column
        self.direction = direction
        self.berries_eaten = 0
        self.asleep = False
        self.turns_asleep = 0
        self.gone = False
        self.announced = False
    

    def __str__(self):
        """Formats the Bear data to a string

        Returns:
            STR: The Bear data in a string.
        """
        bear_string = "Bear at ({0},{1}) moving {2}".format(
            self.row, 
            self.column, 
            self.direction
            )
        
        if self.gone:
            bear_string += " - Left the Field"
        elif self.asleep:
            bear_string += " - Asleep for {} more turns".format(3 - self.turns_asleep)
        
        return bear_string
            
        
    def move(self, b_field):
        """Moves the bear until it has eaten 30 berries or eats a tourist.

        Args:
            b_field (BerryField): The berry field object.
        """
        if not self.gone:
            self.berries_eaten = 0
            # Keeping track of the waking state of the bear & how many turns
            # it has been asleep
            while not self.asleep and self.berries_eaten < 30:
                # Bear eating the tourist
                if b_field.check_tourist_here(self.row, self.column):
                    self.asleep = True
                else:
                    # The bear eating all the berries on the given location
                    while b_field.field[self.row][self.column] > 0 and \
                        self.berries_eaten < 30:
                            self.berries_eaten += 1
                            b_field.field[self.row][self.column] -= 1
                    
                    # Moving the bear in the given direction
                    if self.berries_eaten < 30:
                        if self.direction.count('N') > 0:
                            self.row -= 1
                            if not self.gone and self.row < 0:
                                self.gone = True
                        elif self.direction.count('S') > 0:
                            self.row += 1
                            if not self.gone and self.row >= len(b_field.field):
                                self.gone = True
                        if self.direction.count('E') > 0:
                            self.column += 1
                            if not self.gone and self.column >= len(b_field.field[self.row]):
                                self.gone = True
                        elif self.direction.count('W') > 0:
                            self.column -= 1
                            if not self.gone and self.column < 0:
                                self.gone = True
                    
                # Checking if the bear has left the field
                if self.gone:
                    b_field.gone_bears.append(self)
                    return
            # Resetting the berries
            if self.berries_eaten == 30:
                self.berries_eaten = 0
            
            # What to do if the Bear is asleep
            if self.asleep:
                self.turns_asleep += 1
                if self.turns_asleep >= 3:
                    # Bear wakes up
                    self.asleep = False
                    self.turns_asleep = 0