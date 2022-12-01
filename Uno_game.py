from tkinter import *
import random
from playsound import playsound
from copy import deepcopy
from abc import ABC, abstractmethod

colorList = ["red", "blue", "green", "yellow"]


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
        

        # dump = dumpPile()
        
        # AI_bot = AI()
        # AI_bot.AI_cards()
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
    

class Card(Sounds):
    def __init__(self):
        super().__init__()
        self.red_imageList = []
        self.blue_imageList = []
        self.green_imageList = []
        self.yellow_imageList = []

        self.red_labelList = []
        self.blue_labelList = []
        self.green_labelList = []
        self.yellow_labelList = []

        self.Card_images()   
        self.Card_setup()
        
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)
    
    def Card_images(self):
        numberList = [i for i in range(10)]
        
        try:
            for i in numberList:
                self.red_imageList.append(PhotoImage(file = f"res/second version/red/red_{str(numberList[i])}.png"))

                self.blue_imageList.append(PhotoImage(file = f"res/second version/blue/blue_{str(numberList[i])}.png"))

                self.green_imageList.append(PhotoImage(file = f"res/second version/green/green_{str(numberList[i])}.png"))

                self.yellow_imageList.append(PhotoImage(file = f"res/second version/yellow/yellow_{str(numberList[i])}.png"))

        except FileNotFoundError:
            raise FileNotFoundError
        
  
    def Card_setup(self):
    
        for i in range(len(self.red_imageList)):
            self.red_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.red_imageList[i], command= self.click))
            
        for i in range(len(self.blue_imageList)):
            self.blue_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.blue_imageList[i], command= self.click))
         
        for i in range(len(self.green_imageList)):
            self.green_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.green_imageList[i], command= self.click))
         
        for i in range(len(self.yellow_imageList)):
            self.yellow_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.yellow_imageList[i], command= self.click))
         
      
class dumpPile():
    def __init__(self):
        self.dumpPile = []


    
        
class Player(Card):
    def __init__(self):
        super().__init__()
        self.player_numberList = []
        self.player_colorList = []

        check_dict = self.player_cards()
        print(check_dict)
        self.place_the_cards()
        
    def player_card_setup(self):
        super().Card_setup()

    def player_cards(self):
        
        self.x = 10
        self.y = 570
        
        i = 0
        
        check_dict = {}
        temp = False

        while(i != 7):
            number = random.randint(0, 9)
            color = random.randint(0,3)
            
            self.player_numberList.append(number)
            self.player_colorList.append(colorList[color])
            
        
            color = self.player_colorList[i]
            number = self.player_numberList[i]
            number_str = str(self.player_numberList[i])
            key = color + f" {number_str}"
            if key in check_dict:
                self.player_colorList.pop()
                self.player_numberList.pop()
                print(Exception("Sorry, No duplicates"))
                continue
                 
                
            check_dict[key] = i

            i += 1
        
        print("player_numberList : ", self.player_numberList)
        print("player_colorList : ", self.player_colorList)
        
        return check_dict
        
    def place_the_cards(self):
        i = 0
        
        while i != len(self.player_colorList):
            color = self.player_colorList[i]
            number = self.player_numberList[i]


            if color == "red":
                card = self.red_labelList[number]
            
            elif color == "blue":
                card = self.blue_labelList[number]
            
            elif color == "green":
                card = self.green_labelList[number]
            
            elif color == "yellow":
                card = self.yellow_labelList[number]
 
            card.place(x = self.x, y = self.y)
            self.x += 80

            i += 1
        
    def click(self, i = -1):
        super().click()
        
        print(i)


# class AI(Card):
#     def __init__(self):
#         super().__init__()
#     
#     def AI_cards(self):
#         x = 10
#         y = 10
#         
#         i = 0
#         list = []
#         temp = False
# 
#         while(i != 7):
#             number = random.randint(0, 9)
# 
#             if number not in list:
#                 list.append(number)
#                 temp = True
#             else:
#                 temp = False
#             
#             if temp == True:
#                 self.Card_put(number, x, y)
#                 x += 80
#                 i += 1
#             else:
#                 continue
#         
# 
            
def main():
    unogui = UnoGUI()

main()