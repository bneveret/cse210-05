from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cycle1 import Cycle1
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.
    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        # self._points = 0
        # self.add_points(0)
        cycle1 = Cycle1()  # added
        self._segment_count = len(cycle1.get_segments())  # Gets the length of the segment list
        self.update_seg_count(self._segment_count)
        # self.add_points(self._segment_count) # Sets up initial segment count
        print(f"count at end of Score's __init__ is {self._segment_count}")  # for debugging

        position = Point(constants.SCORE_X, constants.SCORE_Y)  # Import location of score from Constants file
        self.set_position(position) # Set the position of the score
    
    def update_seg_count(self, segment_count): # new method to replace add_points
        """Adds the given points to the score's total points.
        
        Args:
            segment_count: the number of segments
        """
        self._seg_count = segment_count
        self.set_text(f"Segments Created: {self._seg_count}")  # Updated to show Segments created instead of points
        print(f"count at end of Score's update_seg_count method is {self._seg_count}")  # for debugging
    
    
    # ideally the method below will not be needed, depending on what happens 
    # in other classes and methods as we modify the program
    #def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        
    #   self._points += points
    #   self.set_text(f"Segments Created: {self._points}")  # Updated to show Segments created instead of points