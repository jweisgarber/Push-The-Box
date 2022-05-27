import pyray
import constants

class VideoService():
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new instance of VideoService
        
        Args:
            debug (bool): Whether to draw in debug mode or not.
        """
        self._debug = debug

    def open_window(self):
        """Opens a new game window with the provided title"""

        pyray.init_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)
        pyray.set_target_fps(constants.FRAMERATE)

    def close_window(self):
        """Closes the window and releases all computing resources."""

        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_shape(self, shape):
        """Draws the given shape to the screen.
        Args:
            shape (Actor): an instance of actor"""
        if isinstance(shape, object):
            x = shape.get_position().get_x()
            y = shape.get_position().get_y()
            width = shape.get_width()
            height = shape.get_height()
            color = shape.get_color()
            type = shape.get_type()

            if type == "rect":
                pyray.draw_rectangle(x, y, width, height, color)
            elif type == "circle":
                pyray.draw_circle(x, y, width/2, color)

    def draw_shapes(self, shapes):
        """Draws a list of shapes to the screen."""
        if isinstance(shapes, list):
            for shape in shapes:
                self.draw_shape(shape)

    def draw_message(self, message, centered = False):
        """Draws the given text to the screen.
        Args:
            message (Actor): An actor containing text
        """
        if isinstance(message, object):
            text = message.get_text()
            x = message.get_position().get_x()
            y = message.get_position().get_y()
            font_size = message.get_font_size()
            color = message.get_color()

            if text == "Push the Box":
                centered = False

            if centered:
                width = pyray.measure_text(text, font_size)
                offset = int(width / 2)
                x -= offset

            pyray.draw_text(text, x, y, font_size, color)

    def draw_messages(self, messages, centered = False):
        if isinstance(messages, list):
            for message in messages:
                self.draw_message(message, centered)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)