from tkinter import *
from variables import *
from cell import Cell

root = Tk()

root.configure(bg="black")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.title("minesweeper game")

top_frame = Frame(
    root, bg="white", width=width_percentage(100), height=height_percentage(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, bg="black", width=width_percentage(25), height=height_percentage(75)
)
left_frame.place(x=0, y=height_percentage(25))

centre_frame = Frame(
    root,
    bg="green",
    width=width_percentage(75),
    height=height_percentage(75),
)

centre_frame.place(x=width_percentage(25), y=height_percentage(25))


for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        c = Cell(x, y)
        c.create_cell_button(centre_frame)
        c.cell_button.grid(
            column=x,
            row=y,
        )

Cell.plant_mine()
Cell.left_label(left_frame)
Cell.top_label(top_frame)


root.mainloop()
