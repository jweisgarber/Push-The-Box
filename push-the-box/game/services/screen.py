import pyray
from json import load

import constants 
from game.casting.actor import Actor
from game.casting.message import Message
from game.shared.point import Point

class Screen:
    """The data that will be displayed to the user.

    The responsibility of Screen is to keep track of which screen is active,
    and which screen to set up next.

    Attributes:
        _screen_name (str): The name of the current screen
        _cast (Cast): The cast of assets
        _levels (dict): A dictionary containing the levels
    """

    def __init__(self, screen_name, cast):
        """Constructs an instance of Screen
        Args:
            screen_name (str): A given screen name
            cast (Cast): The cast of actors
        """
        self._screen_name = screen_name
        self._cast = cast
        self._levels = self._read_levels()
        
    def set_screen_name(self, screen_name):
        """Set the screen name to the given one
        Args:
            screen_name (str): The name of the screen
        """
        self._screen_name = screen_name

    def get_screen_name(self):
        """Get the current screen name
        Return:
            screen_name (str): The name of the current screen
        """
        return self._screen_name

    def _read_levels(self):
        """Read and store levels from a json file."""
        try:
            with open(constants.DATAPATH, "rt") as json_file:
                data = load(json_file)
                return data["Levels"]
        except FileNotFoundError:
            print(FileNotFoundError)

    def setup_screen(self):
        """Set up the screen with all actors for display."""
        # Clear the screen
        self._cast.remove_all_actors()

        # Load the desired screen
        if self._screen_name == "Title Screen":
            self._load_title_screen()

        elif "Level" in self._screen_name:
            self._load_level()

    def _load_title_screen(self):
        """Load the Title Screen."""
        # Set up the Title
        title = Message()
        title.set_text(constants.TITLE)
        title.set_position(Point(10,10))
        title.set_font_size(60)
        title.set_color(pyray.BLUE)

        # Create a start button
        start_text = Message()
        start_text.set_text("Press ENTER to begin playing")
        start_text.set_position(
            Point(int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))
            )
        start_text.set_color(pyray.WHITE)

        # Add the Title and Button to the cast        
        self._cast.add_actor("messages", title)
        self._cast.add_actor("messages", start_text)
        

    def _load_level(self):
        """Load a specific level."""
        self._add_instructions()
        # Get the level
        level = self._levels[self._screen_name]

        for row in range(constants.ROWS):
            for column in range(constants.COLS):
                # Create the walls
                if level[row][column] == "#":
                    wall = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    wall.set_position(position)

                    self._cast.add_actor("background", wall)

                # Create the goal
                elif level[row][column] == "G":
                    goal = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    goal.set_position(position)
                    goal.set_color(pyray.RED)

                    self._cast.add_actor("goal", goal)

                # Create the boxes
                elif level[row][column] == "B":
                    box = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    box.set_position(position)
                    box.set_color(pyray.BEIGE)

                    self._cast.add_actor("boxes", box)

                # Create the player icon
                elif level[row][column] == "P":
                    player = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    player.set_position(position)
                    player.set_color(pyray.WHITE)
                    player.set_type("circle")

                    self._cast.add_actor("player", player)

    def _add_instructions(self):
        """Add instructions to the screen for play."""
        instructions = Message()
        instructions.set_text('"ENTER" -> Next Level'\
            +'   "BACKSPACE" -> Previous Level   "R" -> Reset' \
            +'   "WASD" -> Move')
        instructions.set_font_size(int(constants.FONT_SIZE / 2))
        instructions.set_position(
            Point(int(constants.SCREEN_WIDTH / 2), 15)
            )

        level_name = Message()
        level_name.set_text(self._screen_name)
        level_name.set_font_size(int(constants.FONT_SIZE / 2))
        level_name.set_position(
            Point(int(constants.SCREEN_WIDTH / 2), 0)
            )

        self._cast.add_actor("messages", instructions)
        self._cast.add_actor("messages", level_name)
        