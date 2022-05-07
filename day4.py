from operator import contains
from posixpath import split
import numpy as np
import re

class board:
    marked = np.zeros((5,5))
    self_board = np.zeros((5,5))
    
    # def __init__(self):
    
    def mark(self,row,column):
        self.marked[row][column] = 1

    def is_win(self):
        is_win=False
        for row in range(0,5):
            if(int(self.marked[row][0]) == int(self.marked[row][1]) == int(self.marked[row][2]) == int(self.marked[row][3]) == int(self.marked[row][4]) == 1):
                is_win = True
                return row,0
        # if(is_win == False):
        for column in range(0,5):
            if( int(self.marked[0][column]) == int(self.marked[1][column]) == int(self.marked[2][column]) == int(self.marked[3][column]) == int(self.marked[4][column]) == 1):
                is_win = True
                return 0,column
        return is_win

    def set_self(self,input_matrix):
        for row in range(0,5):
            for column in range(0,5):
                self.self_board[row][column] = int(input_matrix[row][column])





with open("D:/input4.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

order = input[0]
input = input[2:]


for counter in range(0,len(input)):
    input[counter] =  (re.split("\s",input[counter]))

print(input)
# for tedad in range(0,len(input)):
#     table = input[tedad*6][6*tedad+5]

# res = []
# [res.append(x) for x in table[x] if x != '']



# boards = []
# for k in range(1,3):
#     board = board()
#     board.set_self(input[6*k-4:6*k+1])
#     boards[k] = board

    




# print(input[0]) # input
# print(input[1]) # blank
# print(input[2]) # first row
# print(input[3]) # second row
# print(input[4]) # third row
# print(input[5]) # fourth row
# print(input[6]) # fifth row