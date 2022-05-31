from human_player import Human
from computer_player import Computer_player




class Gameplay:
    def __init__(self):
        print ("Welcome to the RPSLS Arena!")
        self.human = Human(input ("Enter your name "))
        self.ai = Computer_player("Piccard")

        pass

    def run_game(self):
        user_input = int (input ("How many user controlled players in this game, 1 or 2? "))
        self.game_intro()
        if user_input == 2:
            self.players_choose_item_round_humans()
        else:
            self.players_choose_item_round()
        
        # self.game_win_scenario()
        
        
        pass

    def players_choose_item_round (self):
        human_wins = 0
        computer_wins = 0
        games_played = 0

        while human_wins < 2 and computer_wins < 2:
            print(f"Round {games_played + 1} is under way!")
            self.human.choose_item()
            self.ai.choose_item()
            if self.human.selected_item == self.ai.selected_item: 
                print ("Its a tie!")
                games_played += 1
            elif self.human.selected_item == "Rock" and self.ai.selected_item == "Scissors":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.ai.selected_item == "Rock":           
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1        
            elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Paper":            
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Rock" and self.ai.selected_item == "Lizard":           
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Spock":         
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.ai.selected_item == "Scissors":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Lizard":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Paper":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.ai.selected_item == "Spock":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.ai.selected_item == "Rock":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            else:
                print (f"{self.ai.name} wins round {games_played +1}!") 
                computer_wins += 1
                games_played += 1  

        if human_wins == 2:
            print (f"{self.human.name} is the victor!")
        elif computer_wins == 2:
            print (f"{self.ai.name} is the victor!")

       
        pass


    def game_intro(self):
        print ("Ok, here are the rules")
        game_rules = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock "]
        for rules in game_rules:
             print (rules)

        pass

    # def game_win_scenario (self):

    def players_choose_item_round_humans(self):
        self.human_two = Human ((input ("Please enter name of player 2 ")))
        
        human_wins = 0
        human_two_wins = 0
        games_played = 0

        while human_wins < 2 and human_two_wins < 2:
            print(f"Round {games_played + 1} is under way!")
            self.human.choose_item()
            self.human_two.choose_item()
            if self.human.selected_item == self.human_two.selected_item: 
                print ("Its a tie!")
                games_played += 1
            elif self.human.selected_item == "Rock" and self.human_two.selected_item == "Scissors":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.human_two.selected_item == "Rock":           
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1        
            elif self.human.selected_item == "Scissors" and self.human_two.selected_item == "Paper":            
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Rock" and self.human_two.selected_item == "Lizard":           
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.human_two.selected_item == "Spock":         
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.human_two.selected_item == "Scissors":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Scissors" and self.human_two.selected_item == "Lizard":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.human_two.selected_item == "Paper":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.human_two.selected_item == "Spock":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.human_two.selected_item == "Rock":
                print (f"{self.human.name} wins round {games_played +1}!")
                human_wins += 1
                games_played += 1
            else:
                print (f"{self.human_two.name} wins round {games_played +1}!") 
                human_two_wins += 1
                games_played += 1  

        if human_wins == 2:
            print (f"{self.human.name} is the victor!")
        elif human_two_wins == 2:
            print (f"{self.human_two.name} is the victor!")

        pass
        

  
    
    