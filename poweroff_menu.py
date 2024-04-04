import os
from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    root.title("Poweroff menu")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root["bg"] = "#282a36"

    style = ttk.Style()
    style.configure("TFrame", background="#050505")
    style.configure("TButton", background="#3b3a39")
    frame = ttk.Frame(root, padding="5 5 5 5")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))

    # Buttons
    pwroff_img = PhotoImage(file="/home/Abner/.Scripts/Poweroff-menu/Power-Off.png")
    power_off = ttk.Button(
        frame, image=pwroff_img, command=lambda: os.system("systemctl poweroff")
    )
    power_off.grid(column=6, row=1, sticky=E)

    rstrt_img = PhotoImage(
        file="/home/Abner/.Scripts/Poweroff-menu/shutdown buttom.png"
    )
    restart = ttk.Button(
        frame,
        image=rstrt_img,
        command=lambda: os.system("systemctl reboot"),
    )
    restart.grid(column=4, row=1, sticky=E)

    lgout_img = PhotoImage(file="/home/Abner/.Scripts/Poweroff-menu/exit-sign.png")
    logout = ttk.Button(frame, image=lgout_img, command=lambda: os.system("kill -9 -1"))
    logout.grid(column=2, row=1, sticky=W)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.after(5000, lambda: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    main()
