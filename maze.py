from cell import Cell
import time, random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):

        if seed is not None:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        if num_cols <= 0:
            raise ValueError("maze must have at least one col")
        if num_rows <= 0:
            raise ValueError("maze must have at least one row")
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for col in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                self._cells[col].append(Cell(self._win))

        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        x1 = self._x1 + row * self._cell_size_x 
        y1 = self._y1 + col * self._cell_size_y
        x2 = self._x1 + (1 + row) * self._cell_size_x
        y2 = self._y1 + (1 + col) * self._cell_size_y
        self._cells[col][row].Draw(x1, y1, x2, y2) 
        self._Animate()

    def _Animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if len(self._cells) > 0 and len(self._cells[0]) > 0:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            col = len(self._cells) - 1
            row = len(self._cells[0]) - 1
            self._cells[col][row].has_bottom_wall = False
            self._draw_cell(col, row)
            self._Animate()

    def _break_walls_r(self, col, row):
        cur_cell = self._cells[col][row]
        cur_cell.visited = True

        while True:
            to_visit = []

            top = 1
            bottom = 2
            left = 3
            right = 4

            top_col = col - 1
            if top_col >= 0:
                if not self._cells[top_col][row].visited: 
                    to_visit.append(top)
            
            bottom_col = col + 1
            if bottom_col < self._num_cols:
                if not self._cells[bottom_col][row].visited: 
                    to_visit.append(bottom)

            left_row = row - 1
            if left_row >= 0:
                if not self._cells[col][left_row].visited: 
                    to_visit.append(left)


            right_row = row + 1
            if right_row < self._num_rows:
                if not self._cells[col][row + 1].visited: 
                    to_visit.append(right)

            if len(to_visit) == 0:
                self._draw_cell(col, row)
                return

            picked = to_visit[random.randrange(0, len(to_visit))]

            if picked == top:
                cur_cell.has_top_wall = False
                self._cells[top_col][row].has_bottom_wall = False
                self._break_walls_r(top_col, row)
            if picked == bottom:
                cur_cell.has_bottom_wall = False
                self._cells[bottom_col][row].has_top_wall = False
                self._break_walls_r(bottom_col, row)
            if picked == left:
                cur_cell.has_left_wall = False
                self._cells[col][left_row].has_right_wall = False
                self._break_walls_r(col, left_row)
            if picked == right:
                cur_cell.has_right_wall = False
                self._cells[col][right_row].has_left_wall = False
                self._break_walls_r(col, right_row)
    

    def _reset_cells_visited(self):
        for col in range(len(self._cells)):
            for row in range(len(self._cells[0])):
                self._cells[col][row].visited = False
    
    def Solve_depth(self):
        return self._solve_r_depth(0, 0)
    
    def _solve_r_depth(self, col, row):
        cur_cell = self._cells[col][row]
        self._Animate()
        cur_cell.visited = True

        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True

        #top
        if (col > 0 
        and not self._cells[col-1][row].visited 
        and not cur_cell.has_top_wall):
            cur_cell.draw_move(self._cells[col-1][row])
            if self._solve_r_depth(col - 1, row) is True:
                return True
            cur_cell.draw_move(self._cells[col-1][row], undo=True)
        
        #bottom
        if (col < self._num_cols -1
        and not self._cells[col+1][row].visited
        and not cur_cell.has_bottom_wall):
            cur_cell.draw_move(self._cells[col+1][row])
            if self._solve_r_depth(col+1, row) is True:
                return True
            cur_cell.draw_move(self._cells[col+1][row], undo=True)
        
        #left
        if (row > 0
        and not self._cells[col][row-1].visited
        and not cur_cell.has_left_wall):
            cur_cell.draw_move(self._cells[col][row-1]) 
            if self._solve_r_depth(col, row-1) is True:
                return True
            cur_cell.draw_move(self._cells[col][row-1], undo=True) 
        
        #right 
        if (row < self._num_rows - 1
        and not self._cells[col][row+1].visited
        and not cur_cell.has_right_wall):
            cur_cell.draw_move(self._cells[col][row+1]) 
            if self._solve_r_depth(col, row+1) is True:
                return True
            cur_cell.draw_move(self._cells[col][row+1], undo=True) 
        
            
        return False

    def Solve_width(self):
        pass
    
