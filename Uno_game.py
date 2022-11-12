from tkinter import *
import random
from playsound import playsound

class UnoGUI:
    def __init__(self):
        window = Tk()
        window.title("Uno Game")

        
        width= 1436
        height= 764
        window.geometry(f"{width}x{height}")
        
        self.imageList = []
        self.imageList.append(PhotoImage(file = "image/test.png"))
        self.imageList.append(PhotoImage(file = "image/test.png"))

        
        print(width, height)
        self.labelList = []
        
        self.labelList.append(Button(window, width= 112, height = 174, borderwidth= 0, image = self.imageList[0], command= self.play))
        self.labelList.append(Button(window, width= 112, height = 174, borderwidth= 0, image = self.imageList[1], command= self.play))

        #self.labelList[0].pack(padx=5, pady=15, side = LEFT)
        #self.labelList[1].pack(padx=5, pady=20, side = LEFT)


        
        self.labelList[0].place(x=100, y=500)
        self.labelList[1].place(x=150, y=500)
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)
        window.mainloop()
        
    def play(self):
        print("hello")
        playsound('image/click.wav', False)

def main():
    unogui = UnoGUI()

main()