import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import raylib

# #encode file to be read by raylib
sound = raylib.LoadSound("snake\game\sounds\lose_sound.wav".encode('ascii'))


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle1 collides
    with the food, or the cycle1 collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle1 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        cycle1 = cast.get_first_actor("cycles1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        cycle2 = cast.get_first_actor("cycles2")
        head2 = cycle2.get_segments() [0]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True           
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True  
        else:
            cycle1.grow_trail(1)
            cycle2.grow_trail(1)
            _seg_count = len(segments1) # get the length of segments for cycle 1
            score.update_seg_count(_seg_count) # send the length of of segments to Score class to update the segments created that is shown on the screen
                    


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle1 and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycles1")
            segments1 = cycle1.get_segments()
            cycle2 = cast.get_first_actor("cycles2")
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            
            #play sound
            raylib.PlaySound(sound)

            for segment in segments1:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)
