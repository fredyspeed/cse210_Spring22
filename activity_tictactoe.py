'''
Author: Fredy Castañeda Sánchez
This activity is a reminder of what I learned in previous courses.
the game is the tic-tac-toe
'''

def main ():
    tic_tac_t = Tictactoe()
    tic_tac_t.fill_board()
    tic_tac_t.print_board()
    win = False
    shots = 0
    while win == False and shots < 9:
        win = tic_tac_t.entry_throw_x()
        if win:
            break
        win = tic_tac_t.entry_throw_o()
        if win:
            break 
        shots+=1
    if(win == False):
        print(f"there is no winner")   
        




class Tictactoe:
    dimentions = 3
    board = []

    def __init__(self, dim = 3): 
        self.dimentions = dim 
        self.board = [[None] * self.dimentions for i in range(self.dimentions)]
  
     
    def fill_board(self):
        countNumber = 1
        for i in range( self.dimentions):  
            for j in range(self.dimentions):
                self.board [i][j] = countNumber
                countNumber+=1
    
    def print_board(self):
        for i in range( self.dimentions):
            for j in range(self.dimentions):
                print(f"{self.board[i][j]}",end="")
                if (j != self.dimentions - 1):
                    print(f"|",end="")
            print()
            if(i < 2):
                for k in range(self.dimentions-1):
                    print(f"-+",end="")
                    if(k == self.dimentions-2):
                        print(f"-")

    def entry_throw_x(self):
        throw_entrie = int( input("x's turn to choose a square (1-9): "))
        if(self.validate_shot(throw_entrie)):
            self.put_shot(throw_entrie,"x")
            self.print_board()
            if(self.there_is_win()):
                print(" x's is the win")
                return True
            else:
                return False
        else:
            print(f" the position {throw_entrie} is invalid or the box is occupied ")
            print(f"choose another position")
            return self.entry_throw_x()
        
    
    def entry_throw_o(self):
        throw_entrie = int (input("o's turn to choose a square (1-9): "))
        if(self.validate_shot(throw_entrie)):
            self.put_shot(throw_entrie,"o")
            self.print_board()
            if(self.there_is_win()):
                print(" o's is the win")
                return True
            else:
                return False
        else:
            print(f" the position {throw_entrie} is invalid or the box is occupied ")
            print(f"choose another position")
            return self.entry_throw_o()

    def validate_shot(self,throw_entrie):
        if(throw_entrie >=1 and throw_entrie <=9):
            if(throw_entrie == 1):
                if(self.board[0][0] == 1):
                    return True
            if(throw_entrie == 2):
                if(self.board[0][1] == 2):
                    return True
            if(throw_entrie == 3):
                if(self.board[0][2] == 3):
                    return True
            if(throw_entrie == 4):
                if(self.board[1][0] == 4):
                    return True
            if(throw_entrie == 5):
                if(self.board[1][1] == 5):
                    return True
            if(throw_entrie == 6):
                if(self.board[1][2] == 6):
                    return True
            if(throw_entrie == 7):
                if(self.board[2][0] == 7):
                    return True
            if(throw_entrie == 8):
                if(self.board[2][1] == 8):
                    return True
            if(throw_entrie == 9):
                if(self.board[2][2] == 9):
                    return True
            return False

    def put_shot(self, throw_entrie, shot):
        if (throw_entrie == 1):
            self.board[0][0] = shot
        elif (throw_entrie == 2):
            self.board[0][1] = shot
        elif (throw_entrie == 3):
            self.board[0][2] = shot
        elif (throw_entrie == 4):
            self.board[1][0] = shot
        elif (throw_entrie == 5):
            self.board[1][1] = shot
        elif (throw_entrie == 6):
            self.board[1][2] = shot
        elif (throw_entrie == 7):
            self.board[2][0] = shot
        elif (throw_entrie == 8):
            self.board[2][1] = shot
        elif (throw_entrie == 9):
            self.board[2][2] = shot

    def there_is_win(self):
        for i in range(self.dimentions):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]):
                return True
            elif(self.board[0][i] == self.board[1][i] == self.board[2][i]):
                return True
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or
           self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return True
        return False


if __name__ == "__main__":
    main()



