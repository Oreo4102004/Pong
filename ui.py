import tkinter

win = tkinter.Tk()
win.title("Pong")
win.geometry("300x53")

def single():
    win.destroy()
    import singleplayer
    if __name__ == "__main__":
        singleplayer
def multi():
    win.destroy()
    multi_win = tkinter.Tk()
    host=tkinter.Label(multi_win,text="IPaddress:").grid(row=0)
    port=tkinter.Label(multi_win, text='Port:').grid(row=1)
    e1 = tkinter.Entry(multi_win)
    e2 = tkinter.Entry(multi_win)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    multi_win.mainloop()


multiplayer = tkinter.Button(text="Multiplayer", width=42,bg="gray",fg="pink",command=multi)
single = tkinter.Button(text="Singleplayer", width=42,command=single,bg="gray",fg="pink")
multiplayer.grid(row=0, column=0)
single.grid(row=1,column=0)

win.mainloop()
