import pygame
from box import Box
from typing import List
class Player:
    def __init__(self, board, position , boxes : List[Box]):
        self.row, self.column = position
        self.board = board
        self.boxes = boxes

    def move(self, direction):

        # Move UP
        if direction == pygame.K_UP:
            if self.board[self.row - 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row -= 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row -1][self.column] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move DOWN
        elif direction == pygame.K_DOWN:
            if self.board[self.row + 1][self.column] == "v":
                self.board[self.row][self.column] = "v"
                self.row += 1  # Update the player's row position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row +1][self.column] == "b" : 
                temp = self.board
                self.board = self.boxes[0].move(direction=direction)
                if temp != self.board:          
                  return self.move(direction)

                print("heloo")

        # Move RIGHT
        elif direction == pygame.K_RIGHT:
            if self.board[self.row][self.column + 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column += 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column +1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        # Move LEFT
        elif direction == pygame.K_LEFT:
            if self.board[self.row][self.column - 1] == "v":
                self.board[self.row][self.column] = "v"
                self.column -= 1  # Update the player's column position
                self.board[self.row][self.column] = "p"
            elif self.board[self.row][self.column -1] == "b" : 
                self.board = self.boxes[0].move(direction=direction)
                return self.move(direction)

        return self.board
