from player import Player
import random

class Computer_player (Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_item(self):
        print ("Computer AI has chosen")
        self.selected_item = random.choice (self.item_list)
        print (f"{self.name} AI has chosen {self.selected_item}")

    def game_win_counter (self):
        self.games_won = 0
        