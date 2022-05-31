from human_player import Human
from computer_player import Computer_player




class Gameplay:
    def __init__(self):
        print ("ROCK, PAPER, SCISSORS, LIZARD, SPOCK")
        print ("Welcome to the RPSLS Arena!")
        self.human = Human(input ("Enter your name "))
        self.ai = Computer_player("Piccard")


        pass

    def run_game(self):
        user_input = int (input ("How many user controlled players in this game? "))
        self.game_intro()
        if user_input == 0:
            self.players_choose_item_round_ai()
        elif user_input == 1:
            self.players_choose_item_one_human()
        else:
            self.players_choose_item_round_two_humans()
        
        # self.game_win_scenario()
        
        
        pass

    def players_choose_item_one_human (self):
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
            print (f"{self.human.name} wins RPSLS!")
        elif computer_wins == 2:
            print (f"{self.ai.name} wins RPSLS!")

        print ("GAME OVER")

       
        pass


    def game_intro(self):
        print (f"Hello {self.human.name}, here are the rules")
        game_rules = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock "]
        for rules in game_rules:
             print (rules)

        pass

    # def game_win_scenario (self):

    def players_choose_item_round_two_humans(self):
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
            print (f"{self.human.name} wins RPSLS!")
        elif human_two_wins == 2:
            print (f"{self.human_two.name} wins RPSLS!")

        print ("GAME OVER")

        pass

    def players_choose_item_round_ai(self):

        self.ai_two = Computer_player ("DATA")
        
        ai_wins = 0
        ai_two_wins = 0
        games_played = 0

        while ai_wins < 2 and ai_two_wins < 2:
            print(f"Round {games_played + 1} is under way!")
            self.ai.choose_item()
            self.ai_two.choose_item()
            if self.ai.selected_item == self.ai_two.selected_item: 
                print ("Its a tie!")
                games_played += 1
            elif self.ai.selected_item == "Rock" and self.ai_two.selected_item == "Scissors":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Paper" and self.ai_two.selected_item == "Rock":           
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1        
            elif self.ai.selected_item == "Scissors" and self.ai_two.selected_item == "Paper":            
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Rock" and self.ai_two.selected_item == "Lizard":           
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Lizard" and self.ai_two.selected_item == "Spock":         
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Spock" and self.ai_two.selected_item == "Scissors":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Scissors" and self.ai_two.selected_item == "Lizard":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Lizard" and self.ai_two.selected_item == "Paper":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Paper" and self.ai_two.selected_item == "Spock":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            elif self.ai.selected_item == "Spock" and self.ai_two.selected_item == "Rock":
                print (f"{self.ai.name} wins round {games_played +1}!")
                ai_wins += 1
                games_played += 1
            else:
                print (f"{self.ai_two.name} wins round {games_played +1}!") 
                ai_two_wins += 1
                games_played += 1  

        if ai_wins == 2:
            print (f"{self.ai.name} wins RPSLS!")
        elif ai_two_wins == 2:
            print (f"{self.ai_two.name} wins RPSLS!")

        print ("GAME OVER")

        pass
        

  
    
    