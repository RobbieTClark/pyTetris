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
win.geometry("480x640")
win.resizable(width=0, height=0)
win.title("Tetris")
win.overrideredirect(1)
win.config(highlightbackground = '#000000')
win.wm_attributes('-transparentcolor','#000000')
win.wm_attributes('-topmost', True)

# Define a Canvas widget
canvas = Canvas(win, width=480, height=640, background = "#000000", highlightthickness=0, borderwidth = 0)
canvas.pack()

label = Label(canvas, borderwidth=0,bg='#000000')
canvas.create_window(0, 0, anchor=NW, window=label)

# Add Images to Canvas widget
image_0 = ImageTk.PhotoImage(Image.open('board_png/tetris_board_blank.png'))
img_0 = canvas.create_image(0, 0, anchor=NW, image=image_0) #-20,-20

image_1 = ImageTk.PhotoImage(Image.open('blocks_png/BlueBlock150.png'))
img_1 = canvas.create_image(21, 18, anchor=NW, image=image_1)

txt_0 = canvas.create_text(100,100, text = "HELLO WORLD", fill = "white", font = ("Courier 15 bold"))

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

# x = 21
# y = 18

# ls = []
# ls_1 = []
# for j in range (20):
#    for i in range(10):
#       ls.append(ImageTk.PhotoImage(Image.open('blocks_jpg/BlueBlock150.jpg')))
#       ls_1.append(canvas.create_image(x + (i * 30), y  + (30 * j), anchor=NW, image=ls[i]))

def left(e):
   x = -30
   y = 0
   canvas.move(img_1, x, y)

def right(e):
   #canvas.delete(img_1)
   x = 30
   y = 0
   canvas.move(img_1, x, y)

def up(e):
   x = 0
   y = -30
   canvas.move(img_1, x, y)

def down(e):
   x = 0
   y = 30
   canvas.move(img_1, x, y)

#Bind the move function
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)

win.mainloop()