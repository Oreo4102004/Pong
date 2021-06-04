import tkinter
from tkinter.constants import W

win = tkinter.Tk()
win.title("Pong")
win.geometry("300x53")

def single():
    win.destroy()
    import singleplayer
    if __name__ == "__main__":
        singleplayer
def multi():
    
multiplayer = tkinter.Button(text="Multiplayer", width=42,bg="gray",fg="pink")
single = tkinter.Button(text="Singleplayer", width=42,command=single,bg="gray",fg="pink")
multiplayer.grid(row=0, column=0)
single.grid(row=1,column=0)

win.mainloop()
