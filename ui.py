import pygame

class UserInterface:
    def __init__(self, window, Board):
        self.window = window 
        self.playing = True  
        self.squareSize = 100  
        self.pieces = 64
        self.initialX = 0
        self.initialY = 0       
        self.finalX = 0
        self.finalY = 0
        self.chessboard = Board 
        self.userMove = ""  
        self.aiMove = "" 
        self.userColour = "" 
        self.aiColour = "" 

    def drawBoard(self):
        for i in range(0, self.pieces, 2):
            pygame.draw.rect(self.window, (255, 255, 255), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])
            pygame.draw.rect(self.window, (100, 100, 100), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])
        for index in range(self.pieces):
            currentPosition = self.chessboard.board[index//8][index % 8] 
            if currentPosition == "P":
                chessPieces = pygame.image.load("img/pawn_white.png")
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize)) 
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "p":
                chessPieces = pygame.image.load("img/pawn_black.png")
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize)) 
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "N":
                chessPieces = pygame.image.load("img/knight_white.png")
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize)) 
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "n":        
                chessPieces = pygame.image.load("img/knight_black.png") 
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize)) 
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "B":
                chessPieces = pygame.image.load("img/bishop_white.png")
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize)) 
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "b":
                chessPieces = pygame.image.load("img/bishop_black.png")  
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))           
            elif currentPosition == "R":
                chessPieces = pygame.image.load("img/rook_white.png") 
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
            elif currentPosition == "r":
                chessPieces = pygame.image.load("img/rook_black.png") 
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  
            elif currentPosition == "Q":
                chessPieces = pygame.image.load("img/queen_white.png")  
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  
            elif currentPosition == "q":
                chessPieces = pygame.image.load("img/queen_black.png")
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  
            elif currentPosition == "K":
                chessPieces = pygame.image.load("img/king_white.png") 
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  
            elif currentPosition == "k":
                chessPieces = pygame.image.load("img/king_black.png")  
                chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                self.window.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize)) 
                
        pygame.display.update()


    def handleMove(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False 
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < self.squareSize*8 and pygame.mouse.get_pos()[1] < self.squareSize*8:
                    self.initialX = pygame.mouse.get_pos()[0]
                    self.initialY = pygame.mouse.get_pos()[1] 

            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.finalX = pygame.mouse.get_pos()[0] 
                    self.finalY = pygame.mouse.get_pos()[1]
                    self.calculateMove()  

    def calculateMove(self):
        xInitial = self.initialY//self.squareSize
        yInitial = self.initialX//self.squareSize
        xFinal = self.finalY//self.squareSize
        yFinal = self.finalX//self.squareSize
        if xFinal == 7 and (yInitial == 0 or yInitial == 7) and self.chessboard.board[xInitial][yInitial] == "R" and self.chessboard.board[xFinal][yFinal] == "K":
            if yInitial == 0:
                self.userMove += str(yInitial) + str(yFinal-1) + str(yFinal) + "R" + "C"
            elif yInitial == 7:
                self.userMove += str(yInitial) + str(yFinal+1) + str(yFinal) + "R" + "C"
        else:
            self.userMove += str(xInitial) + str(yInitial) + str(xFinal) + str(yFinal) + str(self.chessboard.board[xFinal][(yFinal)])
        if self.userMove in self.chessboard.generateMoveList():
            self.chessboard.calculateMove(self.userMove)
            self.drawBoard() 
            self.aiPlays()
        else:
            print("Move Invalid or Unsafe")
        self.userMove = ""
        self.aiMove = ""

    def aiPlays(self):
        print("AI Turn")
        self.chessboard.changePlayer()
        self.aiMove = self.chessboard.abPruning(self.chessboard.max_depth, float("inf"), -float("inf"), "", 0)
        if self.aiMove is None:
            print("CHECKMATE!")
            self.playing = False
        else:
            self.chessboard.calculateMove(self.aiMove)

        self.chessboard.changePlayer()
        self.drawBoard()

        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.isKingSafe() is False:
                print("CHECKMATE!")
                self.playing = False
                pygame.quit()
            else:
                print("STALEMATE!")
                self.playing = False
                pygame.quit()

        if self.chessboard.isKingSafe() is False:
            print("Check!")

        print("Your Turn")
        

    def playGame(self):
        self.userColour = "W"
        self.aiColour = "B"
        self.drawBoard()
        print("Your Turn")
        while self.playing:
            self.handleMove()