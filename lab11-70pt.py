##########################################
#                                        #
#           70pt - Lab 11                # 
#                                        #
##########################################

# Make the ball twice as large
# Make the ball move 5 times faster

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)
circle = drawpad.create_oval(20, 20, 100, 100, fill='green')
direction = 1

def animate():
    global direction

    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5
   
    drawpad.move(circle,direction,0)
    
    drawpad.after(1, animate)


animate()
root.mainloop()
