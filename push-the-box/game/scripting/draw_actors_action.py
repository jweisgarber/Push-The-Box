from game.scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, screen):
        """Execute the Draw Actors Action
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            screen (Screen): The current screen display.
        """
        player = cast.get_first_actor("player")
        boxes = cast.get_actors("boxes")
        goals = cast.get_actors("goal")
        background = cast.get_actors("background")
        messages = cast.get_actors("messages")
        buttons = cast.get_actors("buttons")

        self._video_service.clear_buffer()
        if "Level" in screen.get_screen_name():
            self._video_service.draw_shapes(boxes)
            self._video_service.draw_shapes(goals)
            self._video_service.draw_shape(player)
            self._video_service.draw_shapes(background)
        self._video_service.draw_shapes(buttons)
        self._video_service.draw_messages(messages, centered = True)
        self._video_service.flush_buffer()