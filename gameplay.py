from human_player import Human
from computer_player import Computer_player

class Gameplay:
    def __init__(self):
        self.human = Human(input ("Enter your name "))
        self.ai = Computer_player("Piccard")

        pass

    def run_game(self):
        human_counter = 0
        computer_counter = 0
        print ("Welcome to the RPSLS Arena!")
        user_input = (input ("How many user controlled players in this game? "))
        self.game_intro()
        self.players_choose_item_round_one()
        # self.players_choose_item_round_two()
        # self.game_showdown()
        if human_counter == 1:
            print (f"GAME OVER! {self.human.name} IS VICTORIUS ")
        pass

    def players_choose_item_round_one (self):
        print("Round 1 is under way")
        self.human.choose_item()
        self.ai.choose_item()
        if self.human.selected_item == self.ai.selected_item:
            print ("Its a tie!")
        elif self.human.selected_item == "Rock" and self.ai.selected_item == "Scissors":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Paper" and self.ai.selected_item == "Rock":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Paper":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Rock" and self.ai.selected_item == "Lizard":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Spock":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Spock" and self.ai.selected_item == "Scissors":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Lizard":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Paper":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Paper" and self.ai.selected_item == "Spock":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        elif self.human.selected_item == "Spock" and self.ai.selected_item == "Rock":
            human_counter = 1
            print (f"{self.human.name} WINS!")
        else:
            print (f"{self.ai.name} WINS!")
            computer_counter = 1
        return human_counter

        pass

    def players_choose_item_round_two (self):
        print("Round 2 is under way")
        self.human.choose_item()
        self.ai.choose_item()
        pass

    def game_intro(self):
        print ("Ok, here are the rules")
        game_rules = [ "Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock "]
        for rules in game_rules:
             print (rules)

        pass

  
    