from tkinter import *
import random
from playsound import playsound
import random


colorList = ["red", "blue", "green", "yellow"]
numberList = [i for i in range(10)]

class UnoGUI:
    def __init__(self):
        window = Tk()
        window.title("Uno Game")

        window.configure(bg="blue")
        width= 1436
        height= 764
        window.geometry(f"{width}x{height}")
    

        
        self.imageList = []
        self.imageList.append(PhotoImage(file = f"res/second version/red/red_{str(numberList[1])}.png"))
        
        self.imageList.append(PhotoImage(file = f"res/second version/red/red_{str(numberList[2])}.png"))
        
        print(width, height)
        self.labelList = []
        
        self.labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.imageList[0], command= self.click))
        self.labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.imageList[1], command= self.click))

        #self.labelList[0].pack(padx=5, pady=15, side = LEFT)
        #self.labelList[1].pack(padx=5, pady=20, side = LEFT)


        
        self.labelList[0].place(x=100, y=500)
        self.labelList[1].place(x=300, y=500)
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)


        # Draw pile
        bankPhoto = PhotoImage(file = f"res/second version/Back/back1.png")
        backCard = Button(window, width= 80, height = 120, border= 3, image = bankPhoto, command= self.back_click)
        backCard.place(x=1300, y=100)
        window.mainloop()
    
    def player_cards(self):
        print()

    def click(self):
        playsound('res/sounds/mouse_click_close.wav', False)

    # Draw pile 
    def back_click(self):
        playsound('res/sounds/mouse_click_close.wav', False)
        card = random.randint(0, 9)


        self.player_cards(card)



def main():
    unogui = UnoGUI()

main()