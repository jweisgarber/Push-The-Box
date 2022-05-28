import constants, pyray

from game.casting.message import Message
from game.casting.cast import Cast
from game.casting.actor import Actor

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_screen_action import ControlScreenAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.move_actors_action import MoveActorsAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.screen import Screen

from game.shared.point import Point

def main():
    # Set up the Title Screen
    cast = Cast()
    screen_name = "Title Screen"
    
    screen = Screen(screen_name, cast)
    screen.setup_screen()

    # Set up Services
    video_service = VideoService()
    keyboard_service = KeyboardService()

    # Prepare script
    script = Script()
    script.add_action("inputs", ControlActorsAction(keyboard_service))
    script.add_action("inputs", ControlScreenAction())
    script.add_action("updates", MoveActorsAction())
    script.add_action("outputs", DrawActorsAction(video_service))

    # Start Game
    director = Director(video_service, screen)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()