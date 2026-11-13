import tkinter as tk
from tkinter import ttk
import random


state = [[False for x in range(24)] for y in range(24)]

for i in range(28):
    state[random.randrange(0,24)][random.randrange(0,24)] = True

class Application:
    def __init__(self, root):
        self.fag = tk.IntVar()
        self.root = root
        root.title("girp sweper")
        root.geometry("380x480")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 380) // 2}"
            f"+{(root.winfo_screenheight() - 480) // 2}"
        )

        self.separator1 = ttk.Separator(root, orient="horizontal")
        self.separator1.place(x=0, y=80, width=380, height=20)

        self.tittle = tk.Label(root, text="girlpsweeper", font=("MS Mincho", 24, "italic"))
        self.tittle.place(x=0, y=0, width=380, height=90)

        self.buttons = [[0 for x in range(24)] for y in range(24)]

        for x in range(24):
            for y in range(24):
                self.buttons[x][y] = tk.Button(
                    root,
                    text="x",
                    command=lambda x=x, y=y: self.click(x, y)
                )
                #self.buttons[x][y].config(bg="#FFFFFF")
                self.buttons[x][y].place(x=10+15*x, y=80+15*y, width=15, height=15)
                #self.buttons[x][y].bind("<Button-3>", self.rclick)
        self.buttonreset = tk.Button(root, text="reset", command=self.reset)
        self.buttonreset.place(x=10, y=440, width=330, height=30)
        
        
        self.fagbtn = tk.Checkbutton(root, text = "🚩", 
                    variable=self.fag,
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 
        self.fagbtn.place(x=340, y=440, width=30, height=30)

    def click(self,x,y):
        if self.fag.get()==0:
            self.buttons[x][y]["state"] = "disabled"
            if state[x][y]:
                for xr in range(24):
                    for yr in range(24):
                        self.buttons[xr][yr]["state"] = "disabled"
                self.buttons[x][y].config(bg="#FF0000")
                self.buttons[x][y]["text"] = "🧨"
            else:
                nr = 0
                if x>0:
                    if state[x-1][y]:
                        nr+=1
                if x<23:
                    if state[x+1][y]:
                        nr+=1
                if y>0:
                    if state[x][y-1]:
                        nr+=1
                if y<23:
                    if state[x][y+1]:
                        nr+=1
                if x>0 and y>0:
                    if state[x-1][y-1]:
                        nr+=1
                if x<23 and y>0:
                    if state[x+1][y-1]:
                        nr+=1
                if x>0 and y<23:
                    if state[x-1][y+1]:
                        nr+=1
                if x<23 and y<23:
                    if state[x+1][y+1]:
                        nr+=1
                self.buttons[x][y].config(bg="#CACACA")
                if nr==0:
                    self.buttons[x][y]["text"] = " "
                else:
                    self.buttons[x][y]["text"] = str(nr)
        else:
            if state[x][y]:
                self.buttons[x][y]["state"] = "disabled"
                self.buttons[x][y].config(bg="#00FF55")
                self.buttons[x][y]["text"] = "🚩"
            else:
                self.buttons[x][y]["state"] = "disabled"
                self.buttons[x][y].config(bg="#FFEE00")
                self.buttons[x][y]["text"] = "🚩"

    def reset(self):
        for x in range(24):
            for y in range(24):
                self.buttons[x][y]["text"] = "x"
                self.buttons[x][y].config(bg=self.buttonreset.cget("background"))
                self.buttons[x][y]["state"] = "active"
        for xz in range(24):
            for yz in range(24):
                state[xz][yz] = False
        for i in range(28):
            state[random.randrange(0,24)][random.randrange(0,24)] = True




if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
