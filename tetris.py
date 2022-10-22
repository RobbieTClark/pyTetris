from __future__ import annotations
from abc import abstractmethod, ABC
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random

class Block(object):
   x_start, y_start = 36, 36
   def __init__(self, colour, canvas, x , y):
      self.img = ImageTk.PhotoImage(Image.open(f'blocks_png/final/{colour}Block.png'))
      self.canvas = canvas
      self.x = x
      self.y = y
      self.id = self.canvas.create_image(self.x, self.y, anchor=NW, image=self.img, state = HIDDEN) #or normal
   def move(self, x, y):
      self.x += x
      self.y += y
      self.canvas.move(self.id, x, y)
      if self.y >= self.y_start:
         self.canvas.itemconfigure(self.id, state = NORMAL)

class Shape(ABC):
   x_start, y_start = 36, 36
   block_size = 39
   pos_rot_m = np.array([[0,-1], [1, 0]]) 
   neg_rot_m = np.array([[0, 1], [-1, 0]])
   def __init__(self, canvas, colour):
      self.canvas = canvas
      self.colour = colour
      self.y = self.y_start
      self.blocks = []
      self.rotatable = False
      self.make_blocks()
   def move(self, x, y):
      self.y += y
      #if condition:
      #  self.rotatable = True (decorate subclass for condition)
      for block in self.blocks:
         block.move(x, y)
   def make_blocks(self):
      for x, y in self.block_positions:
         self.blocks.append(
            Block(
               self.colour, 
               self.canvas, 
               self.x_start + x*self.block_size, 
               self.y_start-y*self.block_size
            )
         )
   def rotate_clockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_forward[i][0][0]*self.block_size, self.block_displace_forward[i][1][0]*self.block_size)
         self.block_displace_forward[i] = self.pos_rot_m.dot(self.block_displace_forward[i])
         self.block_displace_back[i] = self.pos_rot_m.dot(self.block_displace_back[i])
   def rotate_anticlockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_back[i][0][0]*self.block_size, self.block_displace_back[i][1][0]*self.block_size)
         self.block_displace_back[i] = self.neg_rot_m.dot(self.block_displace_back[i])
         self.block_displace_forward[i] = self.neg_rot_m.dot(self.block_displace_forward[i])

class I_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[2],[-1]]), np.array([[1],[0]]), np.array([[0],[1]]), np.array([[-1],[2]])]
      self.block_displace_back = [np.array([[1],[2]]), np.array([[0],[1]]), np.array([[-1],[0]]), np.array([[-2],[-1]])]
      self.block_positions = [
         [3, 1],
         [4, 1],
         [5, 1],
         [6, 1]]
      super().__init__(canvas, colour)

class L_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[0],[2]]), np.array([[1],[-1]]), np.array([[0],[0]]), np.array([[-1],[1]])]
      self.block_displace_back = [np.array([[-2],[0]]), np.array([[1],[1]]), np.array([[0],[0]]), np.array([[-1],[-1]])]
      self.block_positions = [
         [5, 2],
         [3, 1],
         [4, 1],
         [5, 1]]
      super().__init__(canvas, colour)

class J_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[2],[0]]), np.array([[1],[-1]]), np.array([[0],[0]]), np.array([[-1],[1]])]
      self.block_displace_back = [np.array([[0],[2]]), np.array([[1],[1]]), np.array([[0],[0]]), np.array([[-1],[-1]])]
      self.block_positions = [
         [3, 2],
         [3, 1],
         [4, 1],
         [5, 1]]
      super().__init__(canvas, colour)

class O_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[0],[0]]), np.array([[0],[0]]), np.array([[0],[0]]), np.array([[0],[0]])]
      self.block_displace_back = [np.array([[0],[0]]), np.array([[0],[0]]), np.array([[0],[0]]), np.array([[0],[0]])]
      self.block_positions = [
         [4, 2],
         [5, 2],
         [4, 1],
         [5, 1]]
      super().__init__(canvas, colour)

class S_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[1],[1]]), np.array([[0],[2]]), np.array([[1],[-1]]), np.array([[0],[0]])]
      self.block_displace_back = [np.array([[-1],[1]]), np.array([[-2],[0]]), np.array([[1],[1]]), np.array([[0],[0]])]
      self.block_positions = [
         [4, 2],
         [5, 2],
         [3, 1],
         [4, 1]]
      super().__init__(canvas, colour)

class T_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[1],[1]]), np.array([[1],[-1]]), np.array([[0],[0]]), np.array([[-1],[1]])]
      self.block_displace_back = [np.array([[-1],[1]]), np.array([[1],[1]]), np.array([[0],[0]]), np.array([[-1],[-1]])]
      self.block_positions = [
         [4, 2],
         [3, 1],
         [4, 1],
         [5, 1]]
      super().__init__(canvas, colour)

class Z_Block(Shape):
   def __init__(self, canvas, colour):
      self.block_displace_forward = [np.array([[2],[0]]), np.array([[1],[1]]), np.array([[0],[0]]), np.array([[-1],[1]])]
      self.block_displace_back = [np.array([[0],[2]]), np.array([[-1],[1]]), np.array([[0],[0]]), np.array([[-1],[-1]])]
      self.block_positions = [
         [3, 2],
         [4, 2],
         [4, 1],
         [5, 1]]
      super().__init__(canvas, colour)

# image_1 = ImageTk.PhotoImage(Image.open('blocks_png/final/BlueBlock.png'))
# img_1 = canvas.create_image(35, 36, anchor=NW, image=image_1)   

# if __name__ == "__main__":

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x1000")
win.resizable(width=0, height=0)
win.title("Tetris")
win.overrideredirect(1)
win.config(highlightbackground = '#000000')
win.wm_attributes('-transparentcolor','#000000')
win.wm_attributes('-topmost', True)

# Define a Canvas widget
canvas = Canvas(win, width=700, height=1000, background = "#000000", highlightthickness=0, borderwidth = 0)
canvas.pack()

label = Label(canvas, borderwidth=0,bg='#000000')
canvas.create_window(0, 0, anchor=NW, window=label)

# Add Images to Canvas widget
image_0 = ImageTk.PhotoImage(Image.open('board_png/final/tetris_board_removed_comp.png'))
img_0 = canvas.create_image(0, 0, anchor=NW, image=image_0) #-20,-20

#l_block = L_Block(canvas)
#i_block = I_Block(canvas)
#j_block = J_Block(canvas)
#o_block = O_Block(canvas)
#s_block = S_Block(canvas)
#t_block = T_Block(canvas)
z_block = Z_Block(canvas, "Red")

colour_picker = [
   "Blue",
   "Green", 
   "Orange", 
   "Purple", 
   "Red", 
   "Yellow"]

shape_picker = [
   "",
]


#txt_0 = canvas.create_text(100,100, text = "HELLO WORLD", fill = "white", font = ("Courier 15 bold"))

offsetx = 0
offsety = 0

def drag(event):
    x = win.winfo_pointerx() - win.offsetx
    y = win.winfo_pointery() - win.offsety
    win.geometry('+{x}+{y}'.format(x=x,y=y))

def click(event):
    win.offsetx = event.x
    win.offsety = event.y 

win.bind('<Button-1>', click)
win.bind('<B1-Motion>', drag)

# x = 36
# y = 36

# ls = []
# ls_1 = []
# for j in range (20):
#    for i in range(10):
#       ls.append(ImageTk.PhotoImage(Image.open('blocks_png/final/BlueBlock.png')))
#       ls_1.append(canvas.create_image(x + (i * 39), y  + (39 * j), anchor=NW, image=ls[i]))

def left(e):
   x = -39
   y = 0
   z_block.move(x, y)

def right(e):
   #canvas.delete(img_1)
   x = 39
   y = 0
   z_block.move(x, y)

def up(e):
   x = 0
   y = -39
   z_block.move(x, y)

def down(e):
   x = 0
   y = 39
   z_block.move(x, y)

def rotate_clockwise(e):
   z_block.rotate_clockwise()

def rotate_anticlockwise(e):
   z_block.rotate_anticlockwise()

#Bind the move function

win.bind("<x>", rotate_clockwise)
win.bind("<z>", rotate_anticlockwise)
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)

win.mainloop()