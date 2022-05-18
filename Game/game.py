
import numpy as np
from termcolor import colored

import Components.board
import Components.piece
from gui import Gui

from Components.box import Box
from Components.card import Card


class Game() :

    def __init__(self) :
        self.board = None
        self.center_card = None
        self.player0cards = None
        self.player1cards = None
        self.turn = 0
        self.gui = None

    def getBoard(self) :
        return self.board

    def getCc(self) :
        return self.center_card

    def getP0c(self) :
        return self.player0cards

    def getP1c(self) :
        return self.player1cards

    def getTurn(self) :
        return self.turn    


    def initialize(self) :

        board_matrix = np.array([[Box(),Box(),Box(),Box(),Box()],
                                 [Box(),Box(),Box(),Box(),Box()],
                                 [Box(),Box(),Box(),Box(),Box()],
                                 [Box(),Box(),Box(),Box(),Box()],
                                 [Box(),Box(),Box(),Box(),Box()]])

        for i in range(0,5) :
            for j in range(0,5) :
                board_matrix[i][j].x = i
                board_matrix[i][j].y = j

        for j in range(0,5) :
            pawn = Components.piece.Piece(False,1)
            board_matrix[0][j].setContains(pawn)
            board_matrix[0][j].setFree(False)


        for j in range(0,5) :
            pawn = Components.piece.Piece(False,0)
            board_matrix[4][j].setContains(pawn)
            board_matrix[4][j].setFree(False)

        board_matrix[0][2].getContains().isKing = True
        board_matrix[4][2].getContains().isKing = True

        game_board = Components.board.Board(board_matrix)
        self.board = game_board


        self.gui = Gui(self)
        
        self.center_card, self.player0cards, self.player1cards = self.distribute()

        flag = 0

        while(flag!=1) :
            flag = self.game_turn()
            if(self.turn==1):
                self.turn = 0
            else :
                self.turn = 1

        
    def game_turn(self) :
        
        stayInTurn = 1
        self.gui.draw_board()

        while(stayInTurn != 0) :
            self.gui.call_input()
            userInput = self.gui.getInput()
            inp = userInput.split(" ")
            
            stayInTurn = self.gui.respond(inp)
            
            if(stayInTurn==2) :
                return 1 # RAISE FLAG

        return 0

        


    def distribute(self) :
        cc = Card(np.random.randint(0,16))
        p0c = []
        p1c = []
        a = np.random.randint(0,16)
        b = np.random.randint(0,16)
        c = np.random.randint(0,16)
        d = np.random.randint(0,16)

        while (a == cc.getId()):
            a = np.random.randint(0,16)
        while (b == cc.getId() or b == a):
            b = np.random.randint(0,16)
        while (c == cc.getId() or c == a or c == b):
            c = np.random.randint(0,16)
        while (d == cc.getId() or d == a or d == b or d == c):
            d = np.random.randint(0,16)

        p0c.append(Card(a))
        p1c.append(Card(b))
        p0c.append(Card(c))
        p1c.append(Card(d))
        
        return cc, p0c, p1c




    def playCard(self,id,x,y,x_dest,y_dest) :
        try :
            pieceToMove = self.board.getMatrix()[x,y].getContains()
        except :
            print(colored("Index not in bounds !",'red'))
            return 1

        if(self.board.getMatrix()[x,y].isFree) :
            print(colored("Origin box is free !",'red'))
            return 1

        if(pieceToMove.getColor()!=self.turn) :
            print(colored("This piece is not yours!", 'red'))
            return 1

        L = [l for l in range(0,5)]
        if(x not in L or y not in L) :
            print(colored("Index not in bounds !",'red'))
            return 1

        M = Card(id).getMatrix()
        relativeDest = [x_dest-x,y_dest-y]
        a = relativeDest[0]+2
        if(M[relativeDest[0]+2,relativeDest[1]+2]==0) :
            print(colored("Cannot reach destination with this card !",'red'))
            return 1

        try :
            moveFlag = self.move(pieceToMove,x,y,x_dest,y_dest)
            if(moveFlag==2) :
                return 2
        except :
            print(colored("Did not manage to move piece",'red'))
            return 1

        if (self.turn == 1) :
            if (self.player1cards[0].getId() == id) :
                switchCard = self.player1cards[0]
                self.player1cards[0] = self.center_card
            else :
                switchCard = self.player1cards[1]
                self.player1cards[1] = self.center_card
        else :
            if (self.player0cards[0].getId() == id) :
                switchCard = self.player0cards[0]
                self.player0cards[0] = self.center_card
            else :
                switchCard = self.player0cards[1]
                self.player0cards[1] = self.center_card
        self.center_card = switchCard
        return 0



    def move(self,piece,x,y,x_dest,y_dest):
        mirrorMatrix = self.board.getMatrix()
        mirrorMatrix[x,y].setContains(None)
        mirrorMatrix[x,y].setFree(True)
        if(mirrorMatrix[x_dest,y_dest].isFree==False) :
            winFlag = self.take(mirrorMatrix,x_dest,y_dest)
            if(winFlag == 1):
                return 2
        destBox = Box()
        destBox.setX(x_dest)
        destBox.setY(y_dest)
        destBox.setFree(False)
        destBox.setContains(piece)
        mirrorMatrix[x_dest,y_dest] = destBox

        print(colored("moved piece " + str(x) + str(y) + " to position " + str(x_dest) + str(y_dest), 'green'))
        return 0



    def take(self,M,x,y) :
        if(M[x,y].getContains.isKing) :
            print(colored("PLAYER "+str(self.turn)+" WON !!",'green'))
            return 1
        


## BUG : taking piece destroys origin piece
## TODO : cannot take own piece
## TODO : reverse matrix for player 1 !

