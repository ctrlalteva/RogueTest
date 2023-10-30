import tcod

import random


class Game:
    def __init__(self,
        tileset_path: str,
        screen_width: int,
        screen_height: int
    ):
        self.tileset_path = tileset_path
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tileset = self.create_tileset()
        self.console = self.create_console()
        self.map_seed = 11111
        self.map = self.create_map()

    def create_tileset(self):
        tileset = tcod.tileset.load_tilesheet(
            self.tileset_path,
            columns=16,
            rows=16,
            charmap=tcod.tileset.CHARMAP_CP437
        )
        tcod.tileset.procedural_block_elements(tileset=tileset)
        return tileset

    def create_console(self):
        # create new console
        console = tcod.console.Console(self.screen_width, self.screen_height, order="F")
        console.default_fg = (51, 255, 51)
        return console

    def create_map(self):
        random.seed(self.map_seed)
        new_map = []
        for i in range(0, self.screen_height):
            new_row = []
            for j in range(0, self.screen_width):
                cell_chance = random.random()
                if cell_chance < 0.025:
                    new_row.append("+")
                elif cell_chance < 0.05:
                    new_row.append("o")
                else:
                    new_row.append(".")
            new_map.append(new_row)
        return new_map

    def draw_map(self, console: tcod.console.Console):
        for i in range(0, self.screen_height):
            for j in range(0, self.screen_width):
                    console.print(j, i, self.map[i][j])
        
    def draw_interface(self):
        pass
         

class Map:
    def __init__(self):
        pass

    