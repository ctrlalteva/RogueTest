import tcod

from engine import Game
from event_handler import EventHandler
from player_state import PlayerState


def main():
    # set up tileset and console
    game = Game(
        screen_width=40,
        screen_height=30,
        tileset_path="data/Alloy_curses_12x12.png"
    )
    tileset = game.tileset
    console = game.console

    # create player state
    player_state = PlayerState(
        player_x=console.width // 2,
        player_y=console.height // 2
    )

    # create event handler
    event_handler = EventHandler(player_state)

    # create new window and manage context
    with tcod.context.new(
        tileset=tileset,
        console=console,
        title="Rogue Test",
        vsync=True
    ) as context:
        # start main game loop
        while True:
            # reset console for update step
            console.clear()

            # update console to show state
            game.draw_map(console)
            player_state.on_draw(console)

            # render the console to the window
            context.present(console)

            # wait for events to handle them
            for event in tcod.event.wait():
                print(event)
                # pass event to player state event handler
                event_handler.on_event(event)


if __name__ == '__main__':
    main()