import tcod

from player_state import PlayerState


class EventHandler:
    def __init__(self, player: PlayerState):
        self.player = player

    def on_event(self, event: tcod.event.Event):
        player_move = [0,0]
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                player_move = [-1, 0]
                self.player.on_move(player_move)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                player_move = [1, 0]
                self.player.on_move(player_move)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                player_move = [0, -1]
                self.player.on_move(player_move)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                player_move = [0, 1]
                self.player.on_move(player_move)