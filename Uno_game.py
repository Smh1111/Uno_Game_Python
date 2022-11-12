from tkinter import *
import random

class UnoGUI:
    def __init__(self):
        window = Tk()
        window.title("Uno Game")

        self.imageList = []
        self.imageList.append(PhotoImage(file = "image/3.png"))

        frame = Frame(window)
        frame.pack()
        

        self.labelList = []
        
        self.labelList.append(Label(frame, image = self.imageList[0], width = 300, height = 900))
        
        self.labelList[0].pack(side = LEFT)

        window.mainloop()
        

def main():
    unogui = UnoGUI()

main()