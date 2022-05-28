import pyray, constants 

from game.shared.point import Point
from game.casting.message import Message
from game.scripting.action import Action

class HandleCollisionsAction(Action):
    """An update action that handles collisions between the actors

    The responsibility of HandleCollisionsAction is to keep track of
    collisions between the different actors and determine what happens
    in each case.

    Attributes:
        _player_collision (bool): The result of a collision involving
            the player
        _box_collision (bool): The result of a collision involving
            the box
        _level_complete (bool): Whether the Level has been completed
            or not
    """

    def __init__(self):
        """Constructs a new instance of HandleCollisionsAction"""
        self._player_collision = False
        self._box_collision = False
        self._level_complete = False

    def execute(self, cast, script, screen):
        """Execute the HandleCollisionsAction.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            screen (Screen): The current screen display.
        """
        # Validate the current screen is a level to continue
        if "Level" not in screen.get_screen_name():
            return

        walls = cast.get_actors("background")
        player = cast.get_first_actor("player")
        boxes = cast.get_actors("boxes")
        goals = cast.get_actors("goal")

        self._player_collision = False
        self._box_collision = False

        for box in boxes:
            # Check collision between box and wall
            for wall in walls:
                if self._check_collision(box, wall):
                    self._box_collision = True
                    return

            # Check collision between box and goal
            for goal in goals:
                if self._check_collision(box, goal):
                    goal.set_color(pyray.DARKGREEN)
                    cast.remove_actor("boxes", box)
                

            # Check collision between player and box
            if self._check_collision(player, box):
                velocity = player.get_velocity()
                box.set_velocity(velocity)

        # Check collision between player and wall
        for wall in walls:
            if self._check_collision(player, wall):
                self._player_collision = True
                return

        if len(boxes) == 0:
            self._level_complete = True
            self._handle_level_complete(cast)
                
    def _check_collision(self, object_1, object_2):
        """Check for a collision between two objects.
        Args:
            object_1 (Actor): The first actor
            object_2 (Actor): The second actor
        """
        position_1 = object_1.get_position()
        position_2 = object_2.get_position()

        return position_1.equals(position_2)
    
    def get_collision(self, type):
        """Return the state of a collision
        Args:
            type (str): The type of collision
        """
        if type == "player":
            return self._player_collision
        if type == "box":
            return self._box_collision

    def _handle_level_complete(self, cast):
        """Update the screen when the level is complete
        Args:
            cast (Cast): The cast of actors
        """
        message = Message()
        message.set_text("Level Complete")
        message.set_position(Point(
            int(constants.SCREEN_WIDTH / 2),
            int(constants.SCREEN_HEIGHT / 2)
            ))
        message.set_color(pyray.BLUE)

        cast.add_actor("messages", message)

class CollisionError(Exception):
    """A custom exception that is raised when an unwanted collision occurs
    """
    pass