from __future__ import annotations
from abc import abstractmethod, ABC
from tkinter import *
from PIL import Image, ImageTk
import numpy as np


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

class I_Block(object):
   x_start, y_start = 36, 36
   block_size = 39
   def __init__(self, canvas):
         self.c_rotation_matrix = np.array([[0,-1], [1, 0]]) 
         self.ac_rotation_matrix = np.array([[0, 1], [-1, 0]])
         self.block_displace_forward = [np.array([[2],[-1]]), np.array([[1],[0]]), np.array([[0],[1]]), np.array([[-1],[2]])]
         self.block_displace_back = [np.array([[1],[2]]), np.array([[0],[1]]), np.array([[-1],[0]]), np.array([[-2],[-1]])]
         self.y = self.y_start
         self.block_positions = [
            [self.x_start+self.block_size*3, self.y_start-self.block_size],
            [self.x_start+self.block_size*4, self.y_start-self.block_size],
            [self.x_start+self.block_size*5, self.y_start-self.block_size],
            [self.x_start+self.block_size*6, self.y_start-self.block_size]]
         self.blocks = []
         self.canvas = canvas
         self.make_blocks()
         self.rotateable = False
   def move(self, x, y):
      self.y += y
      if self.y >= self.y_start + 2*self.block_size:
         self.rotateable = True
      for block in self.blocks:
         block.move(x, y)
   def make_blocks(self):
      for x, y in self.block_positions:
         self.blocks.append(Block("Blue", self.canvas, x, y))
   def rotate_clockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_forward[i][0][0]*self.block_size, self.block_displace_forward[i][1][0]*self.block_size)
         self.block_displace_forward[i] = self.c_rotation_matrix.dot(self.block_displace_forward[i])
         self.block_displace_back[i] = self.c_rotation_matrix.dot(self.block_displace_back[i])
   def rotate_anticlockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_back[i][0][0]*self.block_size, self.block_displace_back[i][1][0]*self.block_size)
         self.block_displace_back[i] = self.ac_rotation_matrix.dot(self.block_displace_back[i])
         self.block_displace_forward[i] = self.ac_rotation_matrix.dot(self.block_displace_forward[i])

class L_Block(object):
   x_start, y_start = 36, 36
   block_size = 39
   def __init__(self, canvas):
      self.c_rotation_matrix = np.array([[0,-1], [1, 0]]) 
      self.ac_rotation_matrix = np.array([[0, 1], [-1, 0]])
      self.block_displace_forward = [np.array([[2],[0]]), np.array([[1],[-1]]), np.array([[0],[0]]), np.array([[-1],[1]])]
      self.block_displace_back = [np.array([[0],[2]]), np.array([[1],[1]]), np.array([[0],[0]]), np.array([[-1],[-1]])]
      self.y = self.y_start
      self.block_positions = [
         [self.x_start+self.block_size*3, self.y_start-self.block_size],
         [self.x_start+self.block_size*3, self.y_start-2*self.block_size],
         [self.x_start+self.block_size*4, self.y_start-self.block_size],
         [self.x_start+self.block_size*5, self.y_start-self.block_size]]
      self.blocks = []
      self.canvas = canvas
      self.make_blocks()
      self.rotateable = False
   def move(self, x, y):
      self.y += y
      if self.y >= self.y_start + 2*self.block_size:
         self.rotateable = True
      for block in self.blocks:
         block.move(x, y)
   def make_blocks(self):
      for x, y in self.block_positions:
         self.blocks.append(Block("Blue", self.canvas, x, y))
   def rotate_clockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_forward[i][0][0]*self.block_size, self.block_displace_forward[i][1][0]*self.block_size)
         self.block_displace_forward[i] = self.c_rotation_matrix.dot(self.block_displace_forward[i])
         self.block_displace_back[i] = self.c_rotation_matrix.dot(self.block_displace_back[i])
   def rotate_anticlockwise(self):
      for i, block in enumerate(self.blocks):
         block.move(self.block_displace_back[i][0][0]*self.block_size, self.block_displace_back[i][1][0]*self.block_size)
         self.block_displace_back[i] = self.ac_rotation_matrix.dot(self.block_displace_back[i])
         self.block_displace_forward[i] = self.ac_rotation_matrix.dot(self.block_displace_forward[i])

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

l_block = L_Block(canvas)
i_block = I_Block(canvas)

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
   i_block.move(x, y)

def right(e):
   #canvas.delete(img_1)
   x = 39
   y = 0
   i_block.move(x, y)

def up(e):
   x = 0
   y = -39
   i_block.move(x, y)

def down(e):
   x = 0
   y = 39
   i_block.move(x, y)

def rotate_clockwise(e):
   i_block.rotate_clockwise()

def rotate_anticlockwise(e):
   i_block.rotate_anticlockwise()

#Bind the move function

win.bind("<x>", rotate_clockwise)
win.bind("<z>", rotate_anticlockwise)
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)

win.mainloop()