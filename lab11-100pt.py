##########################################
#                                        #
#           100pt - Lab 11               # 
#                                        #
##########################################

# Make the ball "wrap" instead of bouncing - when it hits the right
# edge of the window, it should reappear at the left side and continue moving
# to the right. 

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)
circle = drawpad.create_oval(10, 10, 50, 50, fill='black')
direction = 10

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x1 > 800: 
        drawpad.move(circle,-840,10)
    drawpad.move(circle,direction,0)
    drawpad.after(1, animate)


animate()
root.mainloop()
