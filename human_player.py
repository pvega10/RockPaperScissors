from player import Player

class Human (Player):
    def __init__(self,name):
        super().__init__(name)
        self.name = name 

    def choose_item(self):
        for item in self.item_list:
            print (f"Press {self.item_list.index(item) + 1} for {item}")

        user_input = int (input (f" {self.name} make a choice "))
        self.selected_item = self.item_list [user_input - 1]
        print (f"{self.name} has chosen {self.selected_item}")

    def game_win_counter (self):
        self.games_won = 0
        

    pass