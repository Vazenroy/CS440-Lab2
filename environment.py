import numpy as np
import vacuum


class environment():
    #creates environment
    def __init__(self):
        self.env = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    
    def set_HC_env(self):
        self.env = [[0,3,2,0],
               [0,0,0,0],
               [0,4,6,8],
               [7,9,0,10]]
    
    def set_SA_env(self):
        self.env = [[0,3,2,0],
               [3,6,0,0],
               [5,0,6,8],
               [4,9,0,10]]
    
    def insert_vacuum(self, V, row, col):
        V.dirt_level = self.env[row][col]
        V.row = row
        V.col = col
        self.vacuum = V

    def draw_environment(self):
        for row in range(4):
            for col in range(4):
                if row == self.vacuum.row and col == self.vacuum.col:
                    print("V",end=" ")
                else:
                    print(self.env[row][col], end = " ")
            print() # newline

    def get_percept(self, V):
        row = V.row
        col = V.col

        curr = self.env[row][col]
        neighbors = {}
        #check if valid move, if not, it isn't added to percept. 
        if row > 0:
            neighbors['Up'] = self.env[row - 1][col]
        if row < 3:
            neighbors['Down'] = self.env[row + 1][col]
        if col > 0:
            neighbors['Left'] = self.env[row][col - 1]
        if col < 3:
            neighbors['Right'] = self.env[row][col - 1]
        
        return neighbors
# main statement just to prove that it works 
if __name__ == "__main__":
    env = environment()
    env.set_HC_env()
    V = vacuum.vacuum(env)
    env.insert_vacuum(V, 2,2)
    env.draw_environment()
    













        

