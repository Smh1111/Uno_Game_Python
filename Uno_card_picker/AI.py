from Player import Player
import random

class AI(Player):
    def __init__(self, remaining_colors_numbers =  []):
        super().__init__()

        self.remaining_colors_numbers = remaining_colors_numbers
 
        # print(self.remaining_colors_numbers)

        

    def play_random_cards(self):
        ran_card = random.choice(self.remaining_colors_numbers)

        # print("AI Play: ", ran_card)
        self.can_play = False

        return ran_card, self.can_play
        
    