import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsAction(Action):
    """An input action that controls the direction of the player

    The responsibility of ControlActorsAction is to determine the
        velocity of the player

    Attributes:
        keyboard_service (KeyboardService): An instance of KeyboardService
        direction (Point): Velocity of Player
    """

    def __init__(self, keyboard_service):
        """Create a new instance of ControlActorsAction"""
        self._keyboard_service = keyboard_service
        self._direction = Point(0,0)
    
    def execute(self, cast, script, screen):
        """Executes the control actors action

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            screen (Screen): The current screen display
        """
        if "Level" not in screen.get_screen_name():
            return

        # left
        if self._keyboard_service.is_key_pressed('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_pressed('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_pressed('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_pressed('s'):
            self._direction = Point(0, constants.CELL_SIZE)

        # Set direction
        player = cast.get_first_actor("player")
        player.set_velocity(self._direction)
        
        # Reset direction
        self._direction = Point(0,0)
