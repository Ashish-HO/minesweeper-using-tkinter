from tkinter import Button, Label, messagebox
from variables import *
import random


class Cell:
    all = []
    left_cell_count_object = None
    left_cell_count = CELL_COUNT

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_cell_button(self, position):
        btn = Button(
            position,
            height=3,
            width=5,
        )
        btn.bind("<Button-1>", self.left_click_action)
        btn.bind("<Button-3>", self.right_click_action)

        self.cell_button = btn

    def left_click_action(self, event):
        if self.is_mine:
            self.display_mine()
        else:
            num = self.surrounded_mines_length()
            surrounded_cells = self.surrounded_cells_func()
            if num == 0:
                for cell in surrounded_cells:
                    cell.show_cell()
            self.show_cell()

    def get_cell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def surrounded_cells_func(self):
        surrounded_cells = [
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y + 1),
            self.get_cell(self.x + 1, self.y + 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y - 1),
        ]

        surrounded_cells = [cell for cell in surrounded_cells if cell is not None]
        return surrounded_cells

        pass

    def surrounded_mines_length(self):
        counter = 0
        surrounded_cells = self.surrounded_cells_func()
        for cells in surrounded_cells:
            if cells.is_mine:
                counter += 1
        return counter

    def display_mine(self):
        self.cell_button.configure(bg="red")
        messagebox.showwarning("Game Over", "You clicked on mine.")
        exit(0)

    def show_cell(self):
        if not self.is_opened:
            num = self.surrounded_mines_length()
            self.cell_button.configure(text=num)
            Cell.left_cell_count -= 1
            if Cell.left_cell_count_object:
                Cell.left_cell_count_object.configure(
                    text=f"cells left:{Cell.left_cell_count}"
                )
        self.is_opened = True

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_button.configure(bg="blue")
            self.is_mine_candidate = True
        else:
            self.cell_button.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    def __repr__(self):
        return f"cell({self.x},{self.y})"

    @staticmethod
    def plant_mine():
        planned_mines = random.sample(Cell.all, MINES)

        for planned_mine in planned_mines:
            planned_mine.is_mine = True

    @staticmethod
    def left_label(position):
        lbl = Label(position, text=f"cells left:{Cell.left_cell_count}", font=("", 25))
        lbl.place(x=0, y=0)

        Cell.left_cell_count_object = lbl

    @staticmethod
    def top_label(position):
        lbl = Label(position, text="MINESWEEPER", bg="green", font=("Times", 48))
        lbl.pack()
