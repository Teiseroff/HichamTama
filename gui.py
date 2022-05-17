
from multiprocessing.sharedctypes import Value
from termcolor import colored
from Components.card import Card

class Gui():

    def __init__(self, game) :
        self.game = game
        self.userInput = None

    def getInput(self) :
        return self.userInput

    def draw_board(self) :
        board = self.game.getBoard()

        print("\n\n PLAYER " + str(self.game.getTurn()) + " TURN\n")

        print(" =========== ")

        for i in range(0,5) :
            line = []
            line.append("|")
            for j in range(0,5) :
                if (board.getMatrix()[i][j].isFree) :
                    line.append("-")
                else :
                    if (board.getMatrix()[i][j].getContains().isKing) :
                        if (board.getMatrix()[i][j].getContains().color == 0) :
                            line.append("K")
                        else :
                            line.append("C")           
                    else :
                        if (board.getMatrix()[i][j].getContains().color == 0) :
                            line.append("#")
                        else :
                            line.append("X")

            line.append("|")
            print(line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4] + " " + line[5] + " " + line[6])

        print(" =========== \n")

        print("CENTER CARD : " + str(self.game.getCc().getId()))
        print("P0 CARDS: [" + str(self.game.getP0c()[0].getId()) + ", " + str(self.game.getP0c()[1].getId()) + "]")
        print("P1 CARDS: [" + str(self.game.getP1c()[0].getId()) + ", " + str(self.game.getP1c()[1].getId()) + "]\n")


    def call_input(self) :
        self.userInput = input(">> PLAYER " + str(self.game.getTurn()) + " : ")


    def respond(self,inp) :

        if(self.game.getTurn() == 1) :
            playerCards = self.game.getP1c()
        else :
            playerCards = self.game.getP0c()

        if(inp[0] == "card") :
            cardId = int(inp[1])
            mirrorCard = Card(cardId)
            print(mirrorCard.getMatrix())
            return 1

        elif(inp[0] == "play") :
            if(int(inp[1]) == playerCards[0].getId() or int(inp[1]) == playerCards[1].getId()) :
                print(colored("PLAY",'green'))
                if(len(inp)==6):
                    try :
                        inputX = int(inp[2])
                        inputY = int(inp[3])
                        inputDestX = int(inp[4])
                        inputDestY = int(inp[5])
                    except ValueError :
                        print(colored("Mauvais format",'red'))
                        return 1  # STAYINTURN 1
                else :
                    print(colored("Mauvais format",'red'))
                    return 1  # STRAYINTURN 1
                playFlag = self.game.playCard(int(inp[1]),inputX,inputY,inputDestX,inputDestY)
                if(playFlag==1) :
                    return 1
                elif(playFlag==2) :
                    return 2
                else :
                    self.draw_board()
                    return 0 # ON RETOURNE STAYINTURN 0
            else :
                print(colored("Cette carte n'est pas dans votre main !",'red'))
                return 1



        elif(inp[0] == "help") :
            print(colored("Displaying help message",'cyan'))
            return 1

        elif(inp[0] == "exit") :
            print(colored("EXIT",'yellow'))
            return 2

        else :
            print(colored("Commande invalide !",'red'))
            return 1
