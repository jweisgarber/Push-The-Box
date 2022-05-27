class Director():
    """A director for the game

    The responsibility of Director is to control the flow of the game.

    Attributes:
        video_service (VideoService): For providing video output
    """

    def __init__(self, video_service):
        """Construct an instance of Director
        Args:
            video_service (VideoService): An instance of VideoService
        """
        self._video_service = video_service

    def start_game(self, cast, script):
        """Initialize and run the game."""

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self.execute_actions("outputs", cast, script)
        self._video_service.close_window()

    def execute_actions(self, group, cast, script):
        """Execute all actions in a list of actions.
        Args:
            group (str): The name of the group of actions.
            cast (Cast): An instance of cast
            script (Script): An instance of Script
        """
        actions = script.get_actions(group)

        for action in actions:
            action.execute(cast, script)
