from tkinter import *
import random
from playsound import playsound

class UnoGUI:
    def __init__(self):
        window = Tk()
        window.title("Uno Game")

        window.configure(bg="blue")
        width= 1436
        height= 764
        window.geometry(f"{width}x{height}")
        
        self.imageList = []
        self.imageList.append(PhotoImage(file = "res/second version/red/red_1.png"))
        self.imageList.append(PhotoImage(file = "res/second version/red/red_2.png"))
        
        print(width, height)
        self.labelList = []
        
        self.labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.imageList[0], command= self.play))
        self.labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.imageList[1], command= self.play))

        #self.labelList[0].pack(padx=5, pady=15, side = LEFT)
        #self.labelList[1].pack(padx=5, pady=20, side = LEFT)


        
        self.labelList[0].place(x=100, y=500)
        self.labelList[1].place(x=300, y=500)
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)
        window.mainloop()
        
    def play(self):
        print("hello")
        playsound('res/sounds/mouse_click_close.wav', False)

def main():
    unogui = UnoGUI()

main()