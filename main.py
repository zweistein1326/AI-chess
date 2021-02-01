from board import Board
from ui import UserInterface
import pygame

if __name__ == "__main__":
    pygame.init() 
    window = pygame.display.set_mode([800, 800], 0,0)  
    pygame.display.set_caption('AI Chess Single Player')
    Board = Board()
    UI = UserInterface(window, Board)
    UI.playGame() 
    pygame.quit()
