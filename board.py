from copy import deepcopy
from tile import Tile

class Board:
    def __init__(self, config):
        self.config = config
        self.height = 15
        self.width = 15
        self.grid = [[Tile((1+x*30,1+y*30,28,28)) for y in range(self.height)] for x in range(self.width)]
        self.make_configuration(config)
        self.bufferGrid = deepcopy(self.grid)

    def __str__(self):
        return f"<height: {self.height}, width: {self.width}, grid: {[[str(y) for y in x] for x in self.grid]}>"

    def make_configuration(self, config):
        match config:
            case "normal":
                # triple word
                for i in [0, -1]:
                    for j in [4, -5]:
                        self.grid[j][i].set_type('tw')
                        self.grid[i][j].set_type('tw')
                # triple letter
                for i in [0, -1]:
                    for j in [0, -1]:
                        self.grid[j][i].set_type('tl')
                for i in [1, -2]:
                    for j in [5, -6]:
                        self.grid[j][i].set_type('tl')
                        self.grid[i][j].set_type('tl')
                for i in [3, -4]:
                    for j in [3, -4]:
                        self.grid[j][i].set_type('tl')
                for i in [5, -6]:
                    for j in [5, -6]:
                        self.grid[j][i].set_type('tl')
                # double word
                for i in [2, -3]:
                    for j in [2, -3]:
                        self.grid[j][i].set_type('dw')
                for i in [4, -5]:
                    for j in [4, -5]:
                        self.grid[j][i].set_type('dw')
                for i in [3, -4]:
                    self.grid[7][i].set_type('dw')
                    self.grid[i][7].set_type('dw')
                # double letter
                for i in [1, -2]:
                    for j in [1, -2]:
                        self.grid[j][i].set_type('dl')
                for i in [2, -3]:
                    for j in [6, -7]:
                        self.grid[j][i].set_type('dl')
                        self.grid[i][j].set_type('dl')
                for i in [4, -5]:
                    for j in [6, -7]:
                        self.grid[j][i].set_type('dl')
                        self.grid[i][j].set_type('dl')
                for i in [0, -1]:
                    self.grid[7][i].set_type('dl')
                    self.grid[i][7].set_type('dl')
            case "random":
                pass

    def place_letter(self, letter, x, y):
        self.bufferGrid[x][y].letter = letter

    def remove_letter(self, x, y):
        self.bufferGrid[x][y].letter = None

    def clear_word(self):
        self.bufferGrid = deepcopy(self.grid)

    def commit_word(self):
        self.grid = deepcopy(self.bufferGrid)

    def draw(self, screen):
        for column in self.bufferGrid:
            for line in column:
                line.draw(screen)