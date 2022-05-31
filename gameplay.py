from human_player import Human
from computer_player import Computer_player




class Gameplay:
    def __init__(self):
        self.human = Human(input ("Enter your name "))
        self.ai = Computer_player("Piccard")

        pass

    def run_game(self):
       
        print ("Welcome to the RPSLS Arena!")
        user_input = (input ("How many user controlled players in this game? "))
        self.game_intro()
        if user_input == 2:
            self.players_choose_item_round()
        else:
            self.players_choose_item_round_humans()
        
        self.game_win_scenario()
        
        
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
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.ai.selected_item == "Rock":           
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1        
            elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Paper":            
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Rock" and self.ai.selected_item == "Lizard":           
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Spock":         
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.ai.selected_item == "Scissors":
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Scissors" and self.ai.selected_item == "Lizard":
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Lizard" and self.ai.selected_item == "Paper":
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Paper" and self.ai.selected_item == "Spock":
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            elif self.human.selected_item == "Spock" and self.ai.selected_item == "Rock":
                print (f"{self.human.name} WINS!")
                human_wins += 1
                games_played += 1
            else:
                print (f"{self.ai.name} WINS!") 
                computer_wins += 1
                games_played += 1  

       
        pass

    # def players_choose_item_round_two (self):
    #     print("Round 2 is under way")
    #     self.human.choose_item()
    #     self.ai.choose_item()
    #     pass

    def game_intro(self):
        print ("Ok, here are the rules")
        game_rules = [ "Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock "]
        for rules in game_rules:
             print (rules)

        pass

    # def game_win_scenario (self):

    def players_choose_item_round_humans(self):
        print (input ("Please enter name of player 2"))
        

  
    
    