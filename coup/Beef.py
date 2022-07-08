# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:21:08 2022

@author: Daniel Mishler
"""

beef_card_priority = [
    "ambassador",
    "contessa",
    "assassin",
    "captain",
    "duke"]

card_abilities = {
    "duke" :       ["tax", "block_foreign_aid"],
    "captain" :    ["steal", "block_steal"],
    "assassin" :   ["assassinate"],
    "contessa" :   ["block_assassinate"],
    "ambassador" : ["exchange", "block_steal"]
    }

turn_actions = [
    "income",
    "foreign_aid",
    "coup",
    "tax",
    "steal",
    "exchange",
    "assassinate"
    ]

class Player_Beef:
    def __init__(self, name="beef"):
        self.name = name
        self.log = ""
        self.cards = []
        self.coins = 0
    def react(self, hint):
        if hint == "turn":
            game_info = self.get_player_stats(my_turn = True)
            return "income"
        elif hint in ["placeback", "discard"]:
            for consideration in beef_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beef couldn't find a card!")
            return "?"
        elif hint == "challenged":
            log_lines = self.log.split('\n')
            last_line = log_lines[-3]
            action = last_line.split()[1]
            # First, see if he can answer the challenge
            for card in self.cards:
                if action in card_abilities[card]:
                    return card
            # Beef can't answer the challenge.
            print("BEEF: ya got me")
            for consideration in beef_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beef couldn't find a card!")
            return "?"            
        elif hint == "cb?":
            return "pass"
    
    
    # A more refined function that gets all players' cards and coins
    # This will function better than just getting a player who is alive:
    # It will also help identify threats. If you want to use this function,
    # Feel free to go ahead and try it.
    def get_player_stats(self, my_turn = False):
        
        # Find all the players
        first_log_line = self.log.split('\n')[0]
        start_i = first_log_line.find('[')
        end_i = first_log_line.find(']')
        players_string = first_log_line[start_i+1:end_i]
        players_array = players_string.split(", ")
        
        # Build a dictionary of players, each player key leading to another
        # dictionary showing their cards and coins
        players_dict = {}
        for player_name in players_array:
            players_dict[player_name] = {}
            players_dict[player_name]["cards"] = 2
            players_dict[player_name]["coins"] = 2
        
        
        # Man, do I feel like this section is a little sloppy. Relies on
        # some back-looking to see if an action should have applied.
        # Forward-looking would be better if possible.
        intent = None
        recent_round_apply = False
        blocked = challenged = challenge_success = False
        intent_player = intent_target = None
        for line in self.log.split('\n'):
            if line == "":
                # Apply the most recent intent if I already passed my chance
                # to block or challenge.
                recent_round_apply = my_turn
                action = player = target = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
                if action in ["steal", "coup", "assassinate"]:
                    target = line.split()[2]
                else:
                    target = None
            
            if action == "discard":
                players_dict[player]["cards"] -= 1
                
            # *maybe* apply the effects of the action if it's a turn action
            
            # decide whether the previous intent should apply
            apply_intent = False
            if action[:6] == "block_":
                blocked = True
            if action == "challenge":
                challenged = True
                challenger = player
            if action == "discard" and challenged == True:
                if player == challenger:
                    challenge_success = False
                else:
                    challenge_success = True
            if action in turn_actions or recent_round_apply:
                apply_intent = not (blocked ^ challenge_success)
        
            if apply_intent:
                if intent == "income":
                    players_dict[intent_player]["coins"] += 1
                if intent == "foreign_aid":
                    players_dict[intent_player]["coins"] += 2
                if intent == "tax":
                    players_dict[intent_player]["coins"] += 3
                if intent == "steal":
                    steal_coins = min(players_dict[intent_target]["coins"], 2)
                    players_dict[intent_player]["coins"] += steal_coins
                    players_dict[intent_target]["coins"] -= steal_coins
                if intent == "assassinate":
                    players_dict[intent_player]["coins"] -= 3
                if intent == "coup":
                    players_dict[intent_player]["coins"] -= 7
                if intent == "exchange":
                    pass
            
            # Prepare the next intent
            if action in turn_actions:
                intent = action
                intent_player = player
                intent_target = target
                blocked = False
                challenge_success = False
                challenged = False


        # print("prepared players dict:", players_dict)
        turn = 0
        # TODO: properly get the turn number
        game_dict = {}
        game_dict["players"] = players_dict
        game_dict["turn"] = turn
        return game_dict
        
    
    
    def receive(self, message):
        self.log += message
        self.log += "\n"
    
    def show(self, show_cards = False):
        print("player", self.name)
        if show_cards:
            print("cards:", self.cards)
        else:
            print("cards:", len(self.cards))
        print("coins:", self.coins)