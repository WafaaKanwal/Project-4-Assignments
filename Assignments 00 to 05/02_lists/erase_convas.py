import tkinter as tk

# Eraser Tool Application
# This program creates a canvas with a grid of blue cells that can be erased using a "pink eraser" controlled by mouse movement.
# The program uses Tkinter to create a graphical user interface.

# Canvas size and cell size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.create_grid()
        
        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        # Bind mouse movement to eraser function
        self.canvas.bind("<B1-Motion>", self.erase)

    def create_grid(self):
        """Create blue grid cells on the canvas"""
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")
                self.cells.append(cell)

    def erase(self, event):
        """Erase the cells under the eraser"""
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)

        # Check which cells overlap with eraser and turn them white
        overlapping = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        for obj in overlapping:
            if obj in self.cells:  
                self.canvas.itemconfig(obj, fill="white")

# Run Tkinter application
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Eraser Tool")
    EraserCanvas(root)
    root.mainloop()
