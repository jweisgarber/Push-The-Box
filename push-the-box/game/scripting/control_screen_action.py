import pyray

from game.scripting.action import Action

class ControlScreenAction(Action):
    """An input action that controls the screen being displayed

    The responsibility of ControlScreenAction is to determine
    whether to change the screen or reset it.

    Attributes:
        _screen_names (list): A list of all screen names
    """
    
    def __init__(self):
        """Construct a new instance of ControlScreenAction"""
        self._screen_names = [
            "Title Screen",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
            "Level 10",
            "End Screen"
        ]

    def execute(self, cast, script, screen):
        """Execute the ControlScreenAction
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Advance to the next screen
        if pyray.is_key_pressed(pyray.KEY_ENTER):
            # Get the current screen
            current_screen = screen.get_screen_name()
            i_current_screen = self._screen_names.index(current_screen)

            # Get the next screen
            if i_current_screen < 11:
                i_next_screen = i_current_screen + 1
                next_screen = self._screen_names[i_next_screen]
                screen.set_screen_name(next_screen)

            # Set up next screen
            screen.setup_screen()
        
        # Reset Level
        if pyray.is_key_pressed(pyray.KEY_R):
            screen.setup_screen()

        # Return to previous screen
        if pyray.is_key_pressed(pyray.KEY_BACKSPACE):
            # Get the current screen
            current_screen = screen.get_screen_name()
            i_current_screen = self._screen_names.index(current_screen)

            # Get the next screen
            if i_current_screen > 0:
                i_next_screen = i_current_screen - 1
                next_screen = self._screen_names[i_next_screen]
                screen.set_screen_name(next_screen)

            # Set up the screen
            screen.setup_screen()
