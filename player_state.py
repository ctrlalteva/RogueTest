import tcod


class PlayerState:
    def __init__(self, player_x: int, player_y: int):
        self.player_x = player_x
        self.player_y = player_y

    def on_draw(self, console: tcod.console.Console):
        console.print(self.player_x, self.player_y, "@")

    def on_move(self, player_move: list):
        self.player_x += player_move[0]
        self.player_y += player_move[1]