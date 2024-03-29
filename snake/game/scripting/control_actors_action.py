import constants
from game.scripting.action import Action
from game.shared.point import Point

#import all needed info for sound
import raylib
#initialize audio device
raylib.InitAudioDevice()
#encode file to be read by raylib
sound = raylib.LoadSound("snake\game\sounds\player_sound.wav".encode('ascii'))


class ControlActorsAction(Action):
    """
    An input action that controls the cycle1.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle1's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle1 = cast.get_first_actor("cycles1")
        cycle2 = cast.get_first_actor("cycles2")

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            cycle1.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            cycle1.turn_head(self._direction)
            raylib.PlaySound(sound)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            cycle1.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            cycle1.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
            
            
            

       # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            cycle2.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
            cycle2.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
            cycle2.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
            cycle2.turn_head(self._direction)
            #play sound
            raylib.PlaySound(sound)
        

        