import tcod

from engine import GameObject


class EventHandler:
    def __init__(self, player: GameObject):
        self.player = player

    def on_event(self, event: tcod.event.Event):
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                self.player.move(-1, 0)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                self.player.move(1, 0)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                self.player.move(0, -1)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                self.player.move(0, 1)