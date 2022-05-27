import constants, pyray

from game.casting.message import Message
from game.casting.cast import Cast
from game.casting.actor import Actor

from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.video_service import VideoService
from game.services.screen import Screen

from game.shared.point import Point

def main():
    # Set up the Title Screen
    cast = Cast()
    screen_name = "Level 1"
    
    screen = Screen(screen_name, cast)
    screen.setup_screen()

    # Set up Services
    video_service = VideoService()

    # Prepare script
    script = Script()
    script.add_action("outputs", DrawActorsAction(video_service))

    # Start Game
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()