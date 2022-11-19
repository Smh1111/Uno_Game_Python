import tkinter as tk


def pressed():
    print("Button Pressed!")


def create_layout(frame):
    """
    Add two buttons to the frame.
    Both buttons should have the callback (command) pressed, and they should
    have the labels "Button1" and "Button2".
    Args:
      frame (tk.Frame): The frame to create the two buttons in.

    """
    button1 = tk.Button(frame, text="Button1", command=pressed)
    button1.pack(side=tk.TOP, pady=20,  anchor="nw")

    button2 = tk.Button(frame, text="Button2", command=pressed)
    button2.pack(side=tk.TOP, ipadx=20, anchor="nw")

window = tk.Tk()
create_layout(window)

window.mainloop()