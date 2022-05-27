import constants, pyray
from json import load
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

    def __init__(self, screen_name, cast) -> None:
        self._screen_name = screen_name
        self._cast = cast
        self._levels = self._read_levels()
        
    def set_screen_name(self, screen_name):
        """Set the screen name to the given one
        Args:
            screen_name (str): The name of the screen
        """
        self._screen_name = screen_name

    def _read_levels(self):
        try:
            with open(constants.DATAPATH, "rt") as json_file:
                data = load(json_file)
                return data["Levels"]
        except FileNotFoundError:
            print(FileNotFoundError)

    def setup_screen(self):
        if self._screen_name == "Title Screen":
            self._load_title_screen()

        elif self._screen_name == "Level Select":
            self._load_level_select()

        elif self._screen_name == "Level 1":
            self._load_level()

    def _load_title_screen(self):
        # Set up the Title
        title = Message()
        title.set_text(constants.TITLE)
        title.set_position(Point(10,10))
        title.set_font_size(60)
        title.set_color(pyray.BLUE)

        # Create a start button
        start_text = Message()
        start_text.set_text("Start Game")
        start_text.set_position(
            Point(int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))
            )
        start_text.set_color(pyray.WHITE)
        button_width = 180
        button_offset = int(button_width / 2)

        start_button = Actor()
        start_button.set_position(
            Point(int((constants.SCREEN_WIDTH / 2) - button_offset),
                int((constants.SCREEN_HEIGHT / 2)))
            )
        start_button.set_height(constants.CELL_SIZE)
        start_button.set_width(button_width)
        start_button.set_color(pyray.RED)

        # Add the Title and Button to the cast        
        self._cast.add_actor("messages", title)
        self._cast.add_actor("messages", start_text)
        self._cast.add_actor("buttons", start_button)

    def _load_level(self):
        level = self._levels[self._screen_name]

        for row in range(constants.ROWS):
            for column in range(constants.COLS):
                if level[row][column] == "#":
                    wall = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    wall.set_position(position)

                    self._cast.add_actor("background", wall)

                elif level[row][column] == "G":
                    goal = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    goal.set_position(position)
                    goal.set_color(pyray.DARKGREEN)

                    self._cast.add_actor("goal", goal)

                elif level[row][column] == "B":
                    box = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    box.set_position(position)
                    box.set_color(pyray.BEIGE)

                    self._cast.add_actor("boxes", box)

                elif level[row][column] == "P":
                    player = Actor()
                    position = Point(column, row)
                    position = position.scale(constants.CELL_SIZE)
                    player.set_position(position)
                    player.set_color(pyray.WHITE)
                    player.set_type("circle")

                    self._cast.add_actor("player", player)
                    