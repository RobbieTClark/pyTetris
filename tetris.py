# from tkinter import *
# from PIL import Image, ImageTk




# if __name__ == "__main__":
#     win = Tk()
#     win.geometry("750x600")
#     win.title("Tetris")
#     win.mainloop()

# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("520x1020")
win.resizable(width=0, height=0)

# Define a Canvas widget
canvas = Canvas(win, width=500, height=1000, bg="black", highlightthickness=0)
canvas.pack()

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('blocks/purple_O.png'))
img = canvas.create_image(0, 0, anchor=NW, image=image)

def left(e):
   x = -50
   y = 0
   canvas.move(img, x, y)

def right(e):
   x = 50
   y = 0
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -50
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 50
   canvas.move(img, x, y)

# Bind the move function
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)

win.mainloop()