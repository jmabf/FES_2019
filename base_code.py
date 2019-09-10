import heatMap as hm
from tkinter import *

window = Tk()
window.title("FollowSteps")

#window["bg"]         = "blue"
window["background"] = "white"

lb = Label(window, text = "Welcome to FollowSteps")
lb.place(x = 550, y = 250)

#LxA+E+T
#300x300+100+100
window.geometry("1280x720")

prototype = Button(window, width=10, text = "Map", command = hm.heatMap)
prototype.place(x = 575, y = 350)
window.mainloop()

