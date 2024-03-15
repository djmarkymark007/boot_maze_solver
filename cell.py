from graphic import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        #not sure how i want coords passed
        #top left
        self._x1 = None 
        self._y1 = None 
        #bottom right
        self._x2 = None 
        self._y2 = None 
        self._win = window
        self.visited = False
        # if i want to make cross platform some os need "#d9d9d9" check and swap clear_color
        self.clear_color = "white"
       
    def Draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is None:
            return
        #print(self.has_left_wall)
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall, color= self.clear_color)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall, color=self.clear_color)
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall, self.clear_color)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall, self.clear_color)


    def GetMid(self):
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        return (x_mid, y_mid)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid, y_mid = self.GetMid()
        to_x_mid, to_y_mid = to_cell.GetMid()

        fill_color = "red"
        if undo:
            fill_color = "grey"
        # to the left
        if self._x1 > to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x1, y_mid))
            self._win.draw_line(line, fill_color)
            line1 = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line1, fill_color)
        # to the right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line1 = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x1, to_y_mid))
            self._win.draw_line(line1, fill_color)
        # to the top
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line1 = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y2))
            self._win.draw_line(line1, fill_color)
        # to the bottom 
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line1 = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line1, fill_color)

    
    def __repr__(self):
        return f"""top-left:({self._x1}, {self._y1}), bottom-right:({self._x2}, {self._y2}))
has top wall: {self.has_top_wall}
has bottom wall: {self.has_bottom_wall}
has left wall: {self.has_left_wall}
has right wall: {self.has_right_wall}
visited: {self.visited}
"""

