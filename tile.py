import pygame
class Tile:
    def __init__(self, transform):
        self.type = 'normal'
        self.multiplier = 1
        self.letter = None
        self.color = (75, 75, 75)
        self.transform = transform

    def __str__(self):
        return f"<type: {self.type}, multiplier: {self.multiplier}, letter: {self.letter}>"

    def set_type(self, type):
        match type:
            case 'tw':
                self.type = 'word'
                self.multiplier = 3
                self.color = (255,0,0)
            case 'tl':
                self.type = 'letter'
                self.multiplier = 3
                self.color = (0,0,255)
            case 'dw':
                self.type = 'word'
                self.multiplier = 2
                self.color = (150,150,0)
            case 'dl':
                self.type = 'letter'
                self.multiplier = 2
                self.color = (0,255,0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.transform))
        (x, y, sx, sy) = self.transform
        font = pygame.font.Font('fonts/OpenSans-Bold.ttf', sy//2)
        if self.letter != None:
            pygame.draw.rect(screen, (20,20,20), pygame.Rect((x+2,y+2,sx-4,sy-4)))
            text = font.render(self.letter, True, (230,230,230))
        else:
            match (self.type, self.multiplier):
                case ('word', 3):
                    text = font.render('tw', True, (230,230,230))
                case ('letter', 3):
                    text = font.render('tl', True, (230,230,230))
                case ('word', 2):
                    text = font.render('dw', True, (230,230,230))
                case ('letter', 2):
                    text = font.render('dl', True, (230,230,230))
                case _:
                    return
        textRect = text.get_rect()
        textRect.center = (x+sx/2, y+sy/2)
        screen.blit(text, textRect)

