class Peice:
    def __init__(self,Board):
        self.board=Board

    def moveFinder(self,index):
        pass

class Rook(Peice):
    





pawnEvalWhite =[[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],[5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],[1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],[0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],[0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],[0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],[0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]

pawnEvalBlack = pawnEvalWhite[::-1]

knightEval =[[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],[-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],[-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],[-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],[-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],[-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],[-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
    
bishopEvalWhite = [[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],[ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],[ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],[ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],[ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],[ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],[ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]

bishopEvalBlack = bishopEvalWhite[::-1]

rookEvalWhite = [[  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],[  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],[  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]

rookEvalBlack = rookEvalWhite[::-1]

evalQueen =[[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],[ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],[ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],[ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],[  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],[ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],[ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]

kingEvalWhite = [[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],[ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],[ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],[  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],[  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]]

kingEvalBlack = kingEvalWhite[::-1]

print(kingEvalBlack)
