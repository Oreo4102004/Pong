import tkinter

win = tkinter.Tk()
win.title("Pong")
win.geometry("300x70")
win.config(bg="gray")

ip = tkinter.StringVar()
tport = tkinter.StringVar()


def get_something():
    x = ip.get()
    y = port.get()
    print(x, y)


def single():
    win.destroy()
    import singleplayer
    if __name__ == "__main__":
        singleplayer


def multi():
    multiplayer.destroy()
    single.destroy()

    def some():
        tip = ip.get()
        tp = tport.get()
        print(tip, tp)
    host = tkinter.Label(win, text="IP:", bg="gray", fg="pink")
    port = tkinter.Label(win, text="Port", bg="gray", fg="pink")

    e1 = tkinter.Entry(win, textvariable=ip, bg="gray", fg="pink")
    e2 = tkinter.Entry(win, textvariable=tport, bg="gray", fg="pink")

    btn = tkinter.Button(win, text="submit", command=some,
                         bg="gray", fg="pink")
    host.grid(row=0)
    port.grid(row=1)
    btn.grid(row=3)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    # print(ip.get(),port.get())


multiplayer = tkinter.Button(
    text="Multiplayer", width=42, bg="gray", fg="pink", command=multi)
single = tkinter.Button(text="Singleplayer", width=42,
                        command=single, bg="gray", fg="pink")
multiplayer.grid(row=0, column=0)
single.grid(row=1, column=0)

win.mainloop()
