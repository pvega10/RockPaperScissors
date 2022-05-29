from human_player import Human
from computer_player import Computer_player

class Gameplay:
    def __init__(self):
        self.human = Human(input ("Enter your name "))
        self.ai = Computer_player("Piccard")

        pass

    def run_game(self):
        print ("Welcome to the RPSLS Arena!")
        print (input ("How many user controlled players in this game? "))
        self.game_intro()
        self.players_choose_item()
        pass

    def players_choose_item (self):
        self.human.choose_item()
        self.ai.choose_item()
        pass

    def game_intro(self):
        print ("Ok, here are the rules")
        game_rules = [ "Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock "]
        for rules in game_rules:
             print (rules)

        pass
    
    