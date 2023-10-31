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
        for y_coord in range(0, self.screen_height):
            new_row = []
            for x_coord in range(0, self.screen_width):
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
        for y_coord in range(0, self.screen_height):
            for x_coord in range(0, self.screen_width):
                    console.print(x_coord, y_coord, self.map[y_coord][x_coord], self.map_color)


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