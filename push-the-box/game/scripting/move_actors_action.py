from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.handle_collisions_action import HandleCollisionsAction, CollisionError

class MoveActorsAction(Action):
    """An update action that moves all the actors

    The responsibility of MoveActorsAction is to move all actors

    Attributes:
        actors (list): A list of all Actors
        _handle_collisions (HandleCollisionsAction): An instance of 
            HandleCollisionsAction
    """

    def __init__(self):
        """Create an instance of MoveActorsAction"""
        self._actors = []
        self._handle_collisions = HandleCollisionsAction()

    def execute(self, cast, script, screen):
        """Executes the move actors action
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            screen (Screen): The current screen display.
        """
        # Validate the current screen is a level to continue
        if "Level" not in screen.get_screen_name():
            return
            
        player = cast.get_first_actor("player")
        boxes = cast.get_actors("boxes")

        try:
            player.move_next()
            self._handle_collisions.execute(cast, script, screen)
            
            for box in boxes:
                box.move_next()
                box.set_velocity(Point(0,0))

            self._handle_collisions.execute(cast, script, screen)
            
            # The move results in the box or player being in the wall
            if self._handle_collisions.get_collision("player") or \
                    self._handle_collisions.get_collision("box"):
                raise CollisionError
        
        # Undo the movement resulting in an unwanted collision
        except CollisionError:
            velocity = player.get_velocity().reverse()
            player.set_velocity(velocity)
            player.move_next()
            if self._handle_collisions.get_collision("box"):
                box.set_velocity(velocity)
                for box in boxes:
                    box.move_next()
                    box.set_velocity(Point(0,0))
