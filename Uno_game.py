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
        
        AI_bot = AI()
        


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
    

class Card():
    def __init__(self):
        pass
        # self.red_imageList = {}
        # self.blue_imageList = {}
        # self.green_imageList = {}
        # self.yellow_imageList = {}

        # self.red_labelList = []
        # self.blue_labelList = []
        # self.green_labelList = []
        # self.yellow_labelList = []

        
        
        #Label(window, text="first one", bg="#FF0099", fg="white").place(x=75, y=80)
    
    def Card_images(self):
        numberList = [i for i in range(10)]
        
        try:
            for i in numberList:
                self.red_imageList[i] = PhotoImage(file = f"res/second version/red/red_{str(numberList[i])}.png")
                #self.red_imageList.append()

                self.blue_imageList[i] = PhotoImage(file = f"res/second version/blue/blue_{str(numberList[i])}.png")
                #self.blue_imageList.append()

                self.green_imageList[i] = PhotoImage(file = f"res/second version/green/green_{str(numberList[i])}.png")
                #self.green_imageList.append()

                self.yellow_imageList[i] = PhotoImage(file = f"res/second version/yellow/yellow_{str(numberList[i])}.png")
                #self.yellow_imageList.append()

        except FileNotFoundError:
            raise FileNotFoundError
    
   
    def Card_setup(self):
    
        for i in range(len(self.red_imageList)): # i = key
            
            self.red_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.red_imageList[i], command= lambda m = f"{str(i)}": [self.click(f"red {m}")]))
            
        for i in range(len(self.blue_imageList)):
            self.blue_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.blue_imageList[i], command= lambda m = f"{str(i)}": [self.click(f"blue {m}"),]))
         
        for i in range(len(self.green_imageList)):
            self.green_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.green_imageList[i], command= lambda m = f"{str(i)}": [self.click(f"green {m}")]))
         
        for i in range(len(self.yellow_imageList)):
            self.yellow_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.yellow_imageList[i], command= lambda m = f"{str(i)}": [self.click(f"yellow {m}"),]))
        
    def click(self, title):
        playsound('res/sounds/mouse_click_close.wav', False)
        


class dumpPile():
    def __init__(self):
        self.dumpPile = []
 
class Player(Card):
    def __init__(self):
        
        self.player_numberList = []
        self.player_colorList = []

        self.player_red_imageList = {}
        self.player_blue_imageList = {}
        self.player_green_imageList = {}
        self.player_yellow_imageList = {}

        self.player_red_labelList = []
        self.player_blue_labelList = []
        self.player_green_labelList = []
        self.player_yellow_labelList = []

        self.player_check_dict = self.player_cards()
        print(self.player_check_dict)
        self.player_card_setup()
        
    def player_card_images(self):
        numberList = [i for i in range(10)]
        
        try:
            for i in numberList:
                self.player_red_imageList[i] = PhotoImage(file = f"res/second version/red/red_{str(numberList[i])}.png")
                #self.red_imageList.append()

                self.player_blue_imageList[i] = PhotoImage(file = f"res/second version/blue/blue_{str(numberList[i])}.png")
                #self.blue_imageList.append()

                self.player_green_imageList[i] = PhotoImage(file = f"res/second version/green/green_{str(numberList[i])}.png")
                #self.green_imageList.append()

                self.player_yellow_imageList[i] = PhotoImage(file = f"res/second version/yellow/yellow_{str(numberList[i])}.png")
                #self.yellow_imageList.append()

        except FileNotFoundError:
            raise FileNotFoundError

    def player_card_buttons(self):
        self.player_card_images()
        for i in range(len(self.player_red_imageList)): # i = key
            
            self.player_red_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.player_red_imageList[i], command= lambda m = f"{str(i)}": [self.player_click(f"red {m}")]))
            
        for i in range(len(self.player_blue_imageList)):
            self.player_blue_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.player_blue_imageList[i], command= lambda m = f"{str(i)}": [self.player_click(f"blue {m}"),]))
         
        for i in range(len(self.player_green_imageList)):
            self.player_green_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.player_green_imageList[i], command= lambda m = f"{str(i)}": [self.player_click(f"green {m}")]))
         
        for i in range(len(self.player_yellow_imageList)):
            self.player_yellow_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.player_yellow_imageList[i], command= lambda m = f"{str(i)}": [self.player_click(f"yellow {m}"),]))
    
    def player_card_setup(self):
        self.player_card_buttons()
        i = 0
        
        while i != len(self.player_colorList):
            color = self.player_colorList[i]
            number = self.player_numberList[i]


            if color == "red":
                card = self.player_red_labelList[number]
            
            elif color == "blue":
                card = self.player_blue_labelList[number]
            
            elif color == "green":
                card = self.player_green_labelList[number]
            
            elif color == "yellow":
                card = self.player_yellow_labelList[number]
 
            card.place(x = self.x, y = self.y)
            self.x += 80

            i += 1

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
        
    
   
    def player_click(self, title):
        playsound('res/sounds/mouse_click_close.wav', False)
        print("player click: ", title)
        if title in self.player_check_dict:
            print("Player hit")

class AI(Card):
    def __init__(self):
        
        self.AI_numberList = []
        self.AI_colorList = []

        self.AI_red_imageList = {}
        self.AI_blue_imageList = {}
        self.AI_green_imageList = {}
        self.AI_yellow_imageList = {}

        self.AI_red_labelList = []
        self.AI_blue_labelList = []
        self.AI_green_labelList = []
        self.AI_yellow_labelList = []

        check_dict = self.AI_cards()
        print(check_dict)
        self.AI_card_setup()
        
    def AI_card_images(self):
        numberList = [i for i in range(10)]
        
        try:
            for i in numberList:
                self.AI_red_imageList[i] = PhotoImage(file = f"res/second version/red/red_{str(numberList[i])}.png")
                #self.red_imageList.append()

                self.AI_blue_imageList[i] = PhotoImage(file = f"res/second version/blue/blue_{str(numberList[i])}.png")
                #self.blue_imageList.append()

                self.AI_green_imageList[i] = PhotoImage(file = f"res/second version/green/green_{str(numberList[i])}.png")
                #self.green_imageList.append()

                self.AI_yellow_imageList[i] = PhotoImage(file = f"res/second version/yellow/yellow_{str(numberList[i])}.png")
                #self.yellow_imageList.append()

        except FileNotFoundError:
            raise FileNotFoundError

    def AI_card_buttons(self):
        self.AI_card_images()
        for i in range(len(self.AI_red_imageList)): # i = key
            
            self.AI_red_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.AI_red_imageList[i], command= lambda m = f"{str(i)}": [self.AI_click(f"red {m}")]))
            
        for i in range(len(self.AI_blue_imageList)):
            self.AI_blue_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.AI_blue_imageList[i], command= lambda m = f"{str(i)}": [self.AI_click(f"blue {m}"),]))
         
        for i in range(len(self.AI_green_imageList)):
            self.AI_green_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.AI_green_imageList[i], command= lambda m = f"{str(i)}": [self.AI_click(f"green {m}")]))
         
        for i in range(len(self.AI_yellow_imageList)):
            self.AI_yellow_labelList.append(Button(window, width= 80, height = 120, border= 3, image = self.AI_yellow_imageList[i], command= lambda m = f"{str(i)}": [self.AI_click(f"yellow {m}"),]))
    
    def AI_card_setup(self):
        self.AI_card_buttons()
        i = 0
        
        while i != len(self.AI_colorList):
            color = self.AI_colorList[i]
            number = self.AI_numberList[i]


            if color == "red":
                card = self.AI_red_labelList[number]
            
            elif color == "blue":
                card = self.AI_blue_labelList[number]
            
            elif color == "green":
                card = self.AI_green_labelList[number]
            
            elif color == "yellow":
                card = self.AI_yellow_labelList[number]
 
            card.place(x = self.x, y = self.y)
            self.x += 80

            i += 1

    def AI_cards(self):
        
        self.x = 10
        self.y = 10
        
        i = 0
        
        check_dict = {}
        temp = False

        while(i != 7):
            number = random.randint(0, 9)
            color = random.randint(0,3)
            
            self.AI_numberList.append(number)
            self.AI_colorList.append(colorList[color])
            
        
            color = self.AI_colorList[i]
            number = self.AI_numberList[i]
            number_str = str(self.AI_numberList[i])
            key = color + f" {number_str}"
            if key in check_dict:
                self.AI_colorList.pop()
                self.AI_numberList.pop()
                print(Exception("Sorry, No duplicates"))
                continue
                 
                
            check_dict[key] = i

            i += 1
        
        print("AI_numberList : ", self.AI_numberList)
        print("AI_colorList : ", self.AI_colorList)
        
        return check_dict
        
    
   
    def AI_click(self, title):
        playsound('res/sounds/mouse_click_close.wav', False)
        print("AI click: ", title)
        

            
def main():
    unogui = UnoGUI()

main()