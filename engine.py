import tcod

import random


class Game:
    def __init__(self,
        screen_width: int,
        screen_height: int,
        tileset_path: str
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tileset_path = tileset_path
        self.tileset = self.create_tileset()
        self.console = self.create_console()
        self.map_seed = 11111
        self.map = self.create_map()
        self.map_color = (0, 128, 0)

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
        return console

    def create_map(self):
        random.seed(self.map_seed)
        new_map = []
        for y_coord in range(self.screen_height):
            new_map_row = []
            for x_coord in range(self.screen_width):
                cell_chance = random.random()
                if cell_chance < 0.05:
                    new_map_row.append(Tile(block_move=True, block_sight=True, tile_char="o"))
                elif cell_chance < 0.1:
                    new_map_row.append(Tile(block_move=True, block_sight=False, tile_char="+"))
                else:
                    new_map_row.append(Tile(block_move=False, block_sight=False, tile_char="."))
            new_map.append(new_map_row)
        return new_map

    def render_map(self, console: tcod.console.Console):
        for y_coord in range(self.screen_height):
            for x_coord in range(self.screen_width):
                    current_tile = self.map[y_coord][x_coord]
                    console.print(x_coord, y_coord, current_tile.tile_char, fg=self.map_color, bg=None)


class Tile:
    def __init__(self, block_move: bool, block_sight: bool, tile_char: str):
        self.block_move = block_move
        self.block_sight = block_sight
        self.tile_char = tile_char


class GameObject:
    def __init__(
        self,
        obj_x: int,
        obj_y: int,
        char: str,
        color: tuple
    ):
        self.obj_x = obj_x
        self.obj_y = obj_y
        self.char = char
        self.color = color
    
    def move(self, dx, dy):
        #move by the given amount
        self.obj_x += dx
        self.obj_y += dy
    
    def draw(self, target_console: tcod.console.Console):
        #draw the character that represents this object at its position
        target_console.print(x=self.obj_x, y=self.obj_y, string=self.char, fg=self.color)

    def clear(self, target_console: tcod.console.Console):
        #erase the character that represents this object
        target_console.print(x=self.obj_x, y=self.obj_y, string=" ", fg=self.color, bg=None)