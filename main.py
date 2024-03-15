from graphic import Window, Point, Line 
from cell import Cell
from maze import Maze

"""TODO(Mark): maybe try these
    add it to github
    try to implment wilson's algorithm for maze generation
    Add other solving algorithms, like breadth-first search or A*
    Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
    Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
    Make it a game where the user chooses directions
    Time the various algorithms and see which ones are the fastest
"""

if __name__ == "__main__":
    win = Window(800, 600)
    wow = Maze(12, 12, 13, 9, 60, 60, win)
    wow.Solve_depth()

    
    win.wait_for_close()