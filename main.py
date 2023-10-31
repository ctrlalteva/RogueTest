import tcod

from engine import Game, GameObject
from event_handler import EventHandler


def main():
    # set up tileset and console
    game = Game(
        screen_width=40,
        screen_height=30,
        tileset_path="data/Alloy_curses_12x12.png"
    )
    tileset = game.tileset
    root_console = game.console

    # create new window and manage context
    with tcod.context.new(
        tileset=tileset,
        console=root_console,
        title="Rogue Test",
        vsync=True
    ) as context:
        # set up player and npcs
        player = GameObject(root_console.width // 2, root_console.height //2, '@', (255, 255, 255))
        npc = GameObject(root_console.width // 2 - 5, root_console.height //2, '@', (255, 255, 0))
        objects = [npc, player]

        # create event handler
        event_handler = EventHandler(player)
        
        # start main game loop
        while True:
            # reset console for update step
            for obj in objects:
                obj.clear(root_console)
            
            # update console to show state
            game.render_map(root_console)

            # draw all objects on console
            for obj in objects:
                obj.draw(root_console)

            # render the console to the window
            context.present(root_console)

            # wait for events to handle them
            for event in tcod.event.wait():
                print(event)
                # pass event to player state event handler
                event_handler.on_event(event)


if __name__ == '__main__':
    main()