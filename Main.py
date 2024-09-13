import sys
import time
import os
import colorama
from colorama import Fore, Style

colorama.init()

grid = [
    [5, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 2, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 8, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 6, 0, 0, 5],
    [0, 0, 1, 0, 0, 0, 6, 0, 0],
    [2, 0, 0, 5, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 2, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 7, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 9]
]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(Fore.GREEN + "- " * 12 + Style.RESET_ALL)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(Fore.GREEN + "| " + Style.RESET_ALL, end="")
            if grid[i][j] == 0:
                print(Fore.RED + "0 " + Style.RESET_ALL, end="")
            else:
                print(Fore.CYAN + f"{grid[i][j]} " + Style.RESET_ALL, end="")
        print()
    time.sleep(0.05)

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                l[0]=row
                l[1]=col
                return True
    return False

def used_in_row(grid,row,num):
    for i in range(9):
        if(grid[row][i] == num):
            return True
    return False

def used_in_col(grid,col,num):
    for i in range(9):
        if(grid[i][col] == num):
            return True
    return False

def used_in_box(grid,row,col,num):
    for i in range(3):
        for j in range(3):
            if(grid[i+row][j+col] == num):
                return True
    return False

def check_location_is_safe(grid,row,col,num):
    return not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row - row%3,col - col%3,num)

def solve_sudoku(grid):
    l=[0,0]
    if(not find_empty_location(grid, l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(check_location_is_safe(grid,row,col,num)):
            grid[row][col]=num
            print_grid(grid)
            if(solve_sudoku(grid)):
                return True
            grid[row][col]=0
            print_grid(grid)
    return False

if __name__=="__main__":
    if(solve_sudoku(grid)):
        print_grid(grid)
        print(Fore.YELLOW + "Solved :)" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "No Answer :(" + Style.RESET_ALL)
