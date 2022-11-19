from tkinter import *
import random
from playsound import playsound
from copy import deepcopy
from abc import ABC, abstractmethod

colorList = ["red", "blue", "green", "yellow"]
numberList = [i for i in range(10)]

window = Tk()
window.title("Uno Game")

def window_setup():
    
    window.configure(bg="blue")
    width= 1436
    height= 764
    window.geometry(f"{width}x{height}")
    
class UnoGUI:
    def __init__(self):
        window_setup()
        
        player = Player()
        player.player_cards()

        dump = dumpPile()
        
        AI_bot = AI()
        AI_bot.AI_cards()
        # Draw pile
        self.Draw_pile_setup()

        window.mainloop()
        
   
    def Draw_pile_setup(self):
        drawpile = drawPile()


class Sounds(ABC):
    def __init__(self):
        pass

    
    def click(self):
        playsound('res/sounds/mouse_click_close.wav', False)
    
    

class drawPile(Sounds):
    def __init__(self):
        super().__init__()
        bankPhoto = PhotoImage(file = f"res/second version/Back/back1.png")
        backCard = Button(window, width= 80, height = 120, border= 3, image = bankPhoto, command= self.click)
        backCard.place(x=1300, y=100)

        window.mainloop()

    def click(self):
        super().click()
        dump = dumpPile()
        dump.random()

class Card(Sounds):
    def __init__(self):
        super().__init__()
        self.imageList = []
        self.labelList = []

        self.Card_images()   
        self.Card_setup()
        
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)
    
    def Card_images(self):
        for i in numberList:
            self.imageList.append(PhotoImage(file = f"res/second version/red/red_{str(numberList[i])}.png"))
            

    def Card_setup(self):
        for i in range(len(self.imageList)):
            self.labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.imageList[i], command= self.click))
            
    def Card_put(self, card_number, x_value, y_value):
        card = self.labelList[card_number]
        card.place(x = x_value, y = y_value)
        
        
class dumpPile(Card):
    def __init__(self):
        super().__init__()
        
    def random(self):
        number = random.randint(0, 9)
        self.Card_put(number, 800, 300)

    def next_card(self):
        number = random.randint(0, 9)
        self.i += 1
        self.Card_put(number, 500, 350)
        
class Player(Card):
    def __init__(self):
        super().__init__()

    def player_cards(self):
        x = 10
        y = 570
        
        i = 0
        list = []
        temp = False

        while(i != 7):
            number = random.randint(0, 9)

            if number not in list:
                list.append(number)
                temp = True
            else:
                temp = False
            
            if temp == True:
                self.Card_put(number, x, y)
                x += 80
                i += 1
            else:
                continue    
            
    def Play_card(self, card_number):
        card = self.labelList[card_number]
        #card.place(x = x_value, y = y_value)

class AI(Card):
    def __init__(self):
        super().__init__()
    
    def AI_cards(self):
        x = 10
        y = 10
        
        i = 0
        list = []
        temp = False

        while(i != 7):
            number = random.randint(0, 9)

            if number not in list:
                list.append(number)
                temp = True
            else:
                temp = False
            
            if temp == True:
                self.Card_put(number, x, y)
                x += 80
                i += 1
            else:
                continue
        
def main():
    unogui = UnoGUI()

main()