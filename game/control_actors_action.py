import constants
from action import Action
from point import Point


class ControlActorsAction(Action):
    """ This is the input action that controls the snake."""
    
    # The responsibility of "ControlActorsAction" is to get 
    # the direction and move the snake's head.
    """
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        # This Constructs a new "ControlActorsAction" using the 
        # specified KeyboardService.
        """
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        # This Executes the control actors action.
        """
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left movement
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right Movement
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up Movement
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down movement
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)