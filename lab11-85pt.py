##########################################
#                                        #
#           85pt - Lab 11                # 
#                                        #
##########################################

# Make the ball bounce up and down instead of left and right

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)
circle = drawpad.create_oval(300, 300, 400, 400, fill='black')
direction = 5

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(circle)
    if y2 > 600: 
        direction = - 5
    elif y1 < 0:
        direction = 10
    drawpad.move(circle,0,direction)
    drawpad.after(1, animate)


animate()
root.mainloop()
