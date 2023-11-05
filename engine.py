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
        self.map = Map(screen_width, screen_height)
    
    # creates tileset from game tilesheet 
    def create_tileset(self):
        tileset = tcod.tileset.load_tilesheet(
            self.tileset_path,
            columns=16,
            rows=16,
            charmap=tcod.tileset.CHARMAP_CP437
        )
        tcod.tileset.procedural_block_elements(tileset=tileset)
        return tileset

    # creates a console using the game parameters
    def create_console(self):
        # create new console
        console = tcod.console.Console(self.screen_width, self.screen_height, order="F")
        return console


class Map:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_seed = self.set_map_seed()
        self.map_color = (0, 128, 0)
        self.map_data = self.create_map_data()

    # set seed based on system time
    def set_map_seed(self):
        self.map_seed = random.seed()

    # create noise map for map tile data
    def create_noise_map(self):
        noise = tcod.noise.Noise(dimensions=2, seed=self.map_seed)
        noise_grid = noise[tcod.noise.grid(shape=(self.screen_width, self.screen_height), scale=0.25, indexing="ij")]
        noise_grid = (noise_grid + 1.0) * 0.5
        return noise_grid
            
    # generate map data layer
    def create_map_data(self):
        noise_grid = self.create_noise_map()
        new_map = []
        for y_coord in range(self.screen_height):
            new_map_row = []
            for x_coord in range(self.screen_width):
                cell_value = noise_grid[x_coord, y_coord]
                if cell_value < 0.4:
                    new_map_row.append(Tile(block_move=True, block_sight=True, tile_char="o"))
                elif cell_value < 0.2:
                    new_map_row.append(Tile(block_move=True, block_sight=False, tile_char="+"))
                else:
                    new_map_row.append(Tile(block_move=False, block_sight=False, tile_char="."))
            new_map.append(new_map_row)
        return new_map
    
    # render map data layer to console
    def render_map(self, console: tcod.console.Console):
        for y_coord in range(self.screen_height):
            for x_coord in range(self.screen_width):
                    current_tile = self.map_data[y_coord][x_coord]
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
        color: tuple,
        map_data: list
    ):
        self.obj_x = obj_x
        self.obj_y = obj_y
        self.char = char
        self.color = color
        self.map_data = map_data
    
    # move object
    def move(self, dx: int, dy: int):
        if self.obj_x + dx < 0 or self.obj_x + dx >= len(self.map_data[0]):
            return
        if self.obj_y + dy < 0 or self.obj_y + dy >= len(self.map_data):
            return
        
        target_tile = self.map_data[self.obj_y + dy][self.obj_x + dx]
        if not target_tile.block_move:
            self.obj_x += dx
            self.obj_y += dy

    # draw object char on console    
    def draw(self, target_console: tcod.console.Console):
        target_console.print(x=self.obj_x, y=self.obj_y, string=self.char, fg=self.color)

    # make object invisible
    def clear(self, target_console: tcod.console.Console):
        #erase the character that represents this object
        target_console.print(x=self.obj_x, y=self.obj_y, string=" ", fg=self.color, bg=None)