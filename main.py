import pygame, words
from board import Board
from sys import exit

pygame.init()
clock = pygame.time.Clock()
board = Board('normal')
wordlist = words.get_wordlist()
screen = pygame.display.set_mode((board.width*30+1,board.height*30+1))
pygame.display.set_caption('Wordfeud Solver')

while True:
    # Events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: exit()
    
    # Draw
    board.draw(screen)
    pygame.display.flip()    
    clock.tick(30)

    # CLI Input
    try:
        command = input('> ')
        match command[0]:
            case 'p': #place
                (_, l, x, y) = command.split(' ')
                board.place_letter(l,int(x)-1, int(y)-1)
                print('Placed letter.')
            case 'r': #remove
                (_, x, y) = command.split(' ')
                board.remove_letter(int(x)-1, int(y)-1)
                print('Removed letter.')
            case 'c': #commit
                board.commit_word()
                print('word commited.')
            case 'u': #undo
                board.clear_word()
                print('Cleared word.')
            case 'l': #lookup
                pass
            case _:
                print('Invalid input!')
    except:
        print('Invalid input!')