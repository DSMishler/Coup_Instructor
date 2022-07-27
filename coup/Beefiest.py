# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:16:31 2022

@author: Mike
"""



import random
import pickle
import Couptils

beefier_card_priority = [
    "ambassador",
    "captain",
    "contessa",
    "duke",
    "assassin"
    ]

beefeted_card_priority = [
    "ambassador",
    "captain",
    "duke",
    "contessa",
    "assassin"
    ]

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


class Player_Beefiest:
    def __init__(self, name="beefiest"):
        self.name = name
        self.log = ""
        self.cards = []
        self.coins = 0
        self.cb_turn = 0
        try:
            old_memory = open("Player_Beefiest.pkl", "rb")
            self.memory = pickle.load(old_memory)
            old_memory.closed
        except:
            self.memory = {}
            self.memory["games"] = []
            self.memory["opponents"] = {}
        self.mode = "challenge"
    def react(self, hint):
        game_dict = Couptils.log_to_game_dict(self.log)
        game_info = self.get_game_info(my_turn = True)
        #print(game_dict)
        if hint == "turn":
            for player in game_dict["players"]:
                if player == self.name:
                    continue
                else:
                    opponent = player
            # I tried so many times to make this better
            # but for some reason Beef defeated all of my
            # 'smart' strategies using previous game data
            # so this is my copout for Beef
            # this only runs against Beef
            
            if opponent == "beef":
                game_info = self.get_game_info(my_turn = True)
                # Beefeted always taxes turn 1
                if game_info["turn"] == 1:
                    return "tax"
                
                # else, it's not turn 1. What's the next highest priority?
                # Beefeted will swap to get rid of an ambassador
                if "ambassador" in self.cards:
                    return "exchange"
                
                
                # Now, time for Beefeted's objective
                target = self.find_target(game_info)
                if "assassin" in self.cards and self.coins >= 3:
                    return "assassinate " + target
                if self.coins >= 7:
                    return "coup " + target
                
                
                # else just tax
                return "tax"
                
            elif hint in ["placeback", "discard"]:
                for consideration in beefeted_card_priority:
                    for card in self.cards:
                        if card == consideration:
                            return card
                # Error check
                #print("Error: beef couldn't find a card!")
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
                for consideration in beefeted_card_priority:
                    for card in self.cards:
                        if card == consideration:
                            return card
                # Error check
                #print("Error: beef couldn't find a card!")
                return "?"            
            elif hint == "cb?":
                game_info = self.get_game_info(my_turn = False)
                # Always block if you can
                # and always block assassins and foreign aid
                if game_info["cb_state"]["action"] == "foreign_aid":
                    return "block"
                if game_info["cb_state"]["action"] == "assassinate":
                    if game_info["cb_state"]["target"] == self.name:
                        return "block"
                if game_info["cb_state"]["action"] == "steal":
                    if game_info["cb_state"]["target"] == self.name:
                        if "captain" in self.cards or "ambassador" in self.cards:
                            return "block"
                
                # Now for Beefeted's challenges
                # always challenge turn 1 tax
                if game_info["cb_state"]["action"] == "tax":
                    if game_info["turn"] == 1:
                        return "challenge"
                
                
                return "pass"
            
            
            if self.mode == "challenge":
                #do something random
                if self.coins > 9:
                    target = self.find_target(game_dict)
                    return "coup " + target
                if self.coins > 3 and "assassin" in self.cards:
                    target = self.find_target(game_dict)
                    return "assassinate " + target
                if "captain" in self.cards:
                    target = self.find_target(game_dict)
                    return "steal " + target
                if "duke" in self.cards:
                    return "tax"
                if "ambassador" in self.cards:
                    return "exchange"
                else:
                    return "income"
            else:
                # Beefier taxes or does foriegn aid turn 1
                if game_info["turn"] == 1:
                    try:
                        old_memories = (self.memory["opponents"]
                                           [opponent]
                                           ["challenged"]
                                           ["tax"])
                        odds = old_memories["won"]/old_memories["total"]
                        if odds > 0.5:
                            should_I = random.randint(0, 9)
                            if should_I == 0:
                                return "tax"
                        elif "duke" in self.cards:
                            return "tax"
                        else:
                            return "foreign_aid"
                    except:
                        return "tax"
                # else, it's not turn 1.
                if "ambassador" in self.cards:
                    return "exchange"
                
                # find out what people are claiming
                duke_reppers = self.who_claims_dukes()
                for player in duke_reppers:
                    if game_info["players"][player]["cards"] == 0:
                        duke_reppers.remove(player)
                if self.name in duke_reppers:
                    duke_reppers.remove(self.name)
                contessa_reppers = self.who_claims_contessas()
                for player in contessa_reppers:
                    if game_info["players"][player]["cards"] == 0:
                        contessa_reppers.remove(player)
                if self.name in contessa_reppers:
                    contessa_reppers.remove(self.name)
                ambassador_reppers = self.who_claims_ambassadors()
                for player in ambassador_reppers:
                    if game_info["players"][player]["cards"] == 0:
                        ambassador_reppers.remove(player)
                if self.name in ambassador_reppers:
                    ambassador_reppers.remove(self.name)
                captain_reppers = self.who_claims_captains()
                for player in captain_reppers:
                    if game_info["players"][player]["cards"] == 0:
                        captain_reppers.remove(player)
                if self.name in captain_reppers:
                    captain_reppers.remove(self.name)
                assassin_reppers = self. who_claims_assassins()
                for player in assassin_reppers:
                    if game_info["players"][player]["cards"] == 0:
                        assassin_reppers.remove(player)
                if self.name in assassin_reppers:
                    assassin_reppers.remove(self.name)
                
                # it's strategy time
                target = self.find_target(game_dict)
                if "assassin" in self.cards and self.coins >= 3 and len(assassin_reppers) == 0:
                    return "assassinate " + target
                if self.coins >= 7:
                    return "coup " + target
                
                # if I have a captain and odds > .6
                # elif I have a duke tax
                # else just foreign aid
                try:
                    old_memories = (self.memory["opponents"]
                                       [opponent]
                                       ["challenged"]
                                       ["steal"])
                    odds = old_memories["won"]/old_memories["total"]
                    if "captain" in self.cards and odds > .55 and len(captain_reppers) == 0 and len(ambassador_reppers) == 0:
                        return "steal " + target
                    old_memories = (self.memory["opponents"]
                                       [opponent]
                                       ["challenged"]
                                       ["tax"])
                    odds = old_memories["won"]/old_memories["total"]
                    if "duke" in self.cards:
                        return "tax"
                    if odds > 0.55:
                        return "tax"
                    old_memories = (self.memory["opponents"]
                                       [opponent]
                                       ["challenged"]
                                       ["foreign_aid"])
                    odds = old_memories["won"]/old_memories["total"]
                    if odds > .5 and len(duke_reppers) == 0:
                        return "foreign_aid"
                    return "income"
                except:
                    return "foreign_aid"
        elif hint in ["placeback", "discard"]:
            for consideration in beefier_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beefier couldn't find a card!")
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
            for consideration in beefier_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beefier couldn't find a card!")
            return "?"            
        elif hint == "cb?":
            self.cb_turn += 1
            
            duke_reppers = self.who_claims_dukes()
            for player in duke_reppers:
                if game_info["players"][player]["cards"] == 0:
                    duke_reppers.remove(player)
            if self.name in duke_reppers:
                duke_reppers.remove(self.name)
            contessa_reppers = self.who_claims_contessas()
            for player in contessa_reppers:
                if game_info["players"][player]["cards"] == 0:
                    contessa_reppers.remove(player)
            if self.name in contessa_reppers:
                contessa_reppers.remove(self.name)
            ambassador_reppers = self.who_claims_ambassadors()
            for player in ambassador_reppers:
                if game_info["players"][player]["cards"] == 0:
                    ambassador_reppers.remove(player)
            if self.name in ambassador_reppers:
                ambassador_reppers.remove(self.name)
            captain_reppers = self.who_claims_captains()
            for player in captain_reppers:
                if game_info["players"][player]["cards"] == 0:
                    captain_reppers.remove(player)
            if self.name in captain_reppers:
                captain_reppers.remove(self.name)
            assassin_reppers = self. who_claims_assassins()
            for player in assassin_reppers:
                if game_info["players"][player]["cards"] == 0:
                    assassin_reppers.remove(player)
            if self.name in assassin_reppers:
                assassin_reppers.remove(self.name)
                
            if game_dict["this_turn"]["blocker"] is None:
                action = game_dict["this_turn"]["action"]
                target = game_dict["this_turn"]["target"]
                actor = game_dict["this_turn"]["actor"]
                if action == "steal" and target == self.name:
                    # turn 1
                    if self.cb_turn == 1:
                        try:
                            turn1_memories = [self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["income"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["foreign_aid"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["tax"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["steal"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["exchange"]]
                            if turn1_memories[3] > 0.5(turn1_memories[0]
                                                      + turn1_memories[1]
                                                      + turn1_memories[2]
                                                      + turn1_memories[4]
                                                      ):
                                if "captain" in self.cards or "ambassador" in self.cards:
                                    return "block"
                                else:
                                    return "challenge"
                        except:
                            f = ""    
                    if self.mode == "block":
                        return "block"
                    if "captain" in self.cards or "ambassador" in self.cards:
                        return "block"
                    try:
                        old_memories = (self.memory["opponents"]
                                               [opponent]
                                               ["challenged"]
                                               ["block_steal"])
                        odds = old_memories["won"]/old_memories["total"]
                        if odds > .55:
                            return "block"
                    except:
                        return "pass"
                if action == "assassinate" and target == self.name:
                    # turn 1
                    if self.cb_turn == 1:
                        try:
                            turn1_memories = [self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["income"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["foreign_aid"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["tax"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["steal"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["exchange"]]
                            if turn1_memories[3] > 0.5(turn1_memories[0]
                                                      + turn1_memories[1]
                                                      + turn1_memories[2]
                                                      + turn1_memories[4]
                                                      ):
                                if "contessa" in self.cards:
                                    return "block"
                                else:
                                    return "challenge"
                        except:
                            f = ""    
                    if self.mode == "block":
                        return "block"
                    if "contessa" in self.cards:
                        return "block"
                    elif len(self.cards) == 1:
                        return "block"
                    try:
                        old_memories = (self.memory["opponents"]
                                               [opponent]
                                               ["challenged"]
                                               ["block_assassinate"])
                        odds = old_memories["won"]/old_memories["total"]
                        if odds > .55:
                            return "block"
                    except:
                        return "pass"
                if action == "foreign_aid":
                    # turn 1
                    if self.cb_turn == 1:
                        try:
                            turn1_memories = [self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["income"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["foreign_aid"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["tax"],
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["steal"],   
                                              self.memory["opponents"]
                                                    [actor]
                                                    ["turn1"]
                                                    ["exchange"]]
                            if turn1_memories[3] > 0.5(turn1_memories[0]
                                                      + turn1_memories[1]
                                                      + turn1_memories[2]
                                                      + turn1_memories[4]
                                                      ):
                                if "duke" in self.cards:
                                    return "block"
                                else:
                                    return "challenge"
                        except:
                            f = ""    
                    if self.mode == "block":
                        return "block"
                    if "duke" in self.cards:
                        return "block"
                    
                # challenge?
                game_info = self.get_game_info(my_turn = True)
                if game_info["turn"] == 1:
                    should_I = random.randint(0,14)
                    if should_I == 0:
                        return "challenge"
                    else:
                        return "pass"
                try:
                    old_memories = (self.memory["opponents"]
                                           [opponent]
                                           ["challenged"]
                                           ["block_foreign_aid"])
                    odds = old_memories["won"]/old_memories["total"]
                    if odds > .55:
                        return "block"
                except:
                    return "pass"
            else:
                action = "block_"+game_dict["this_turn"]["action"]
            
            if (self.mode == "challenge" and
                action in Couptils.challengeable_actions):
                return "challenge"
            
            
            # decide whether to challenge
            if game_dict["this_turn"]["blocker"] is not None:
                action_in_question = "block_"+game_dict["this_turn"]["action"]
                actor_in_question = game_dict["this_turn"]["blocker"]
            else:
                action_in_question = game_dict["this_turn"]["action"]
                actor_in_question = game_dict["this_turn"]["actor"]
            
            try:
                old_memories = (self.memory["opponents"]
                                       [actor_in_question]
                                       ["challenged"]
                                       [action_in_question])
                odds = old_memories["won"]/old_memories["total"]
                if action_in_question == "tax":
                    if odds > 0.55 and len(duke_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "steal":
                    if odds > 0.55 and len(captain_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "exchange":
                    if odds > 0.55 and len(ambassador_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "assassinate":
                    if odds > 0.55 and len(assassin_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "block_steal":
                    if odds > 0.55 and len(captain_reppers) == 0 and len(ambassador_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "block_assassinate":
                    if odds > 0.55 and len(contessa_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
                if action_in_question == "block_foreign_aid":
                    if odds > 0.55 and len(duke_reppers) == 0:
                        return "challenge"
                    else:
                        return "pass"
            except KeyError:
                return "pass"

            return "pass"
        else:
            print("error: unknown hint for reaction!")
            return "?"
    
    
    # A more refined function that gets all players' cards and coins
    # This will function better than just getting a player who is alive:
    # It will also help identify threats. If you want to use this function,
    # Feel free to go ahead and try it.
    def get_game_info(self, my_turn = False):
        
        # Turns start with turn 1 - it becomes turn 1 as soon as the
        # first player acts.
        turn = 0
        
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
            players_dict[player_name]["claims"] = []
        
        
        cb_state= {} # challenge/block state information
        # Note: This information may not *always* be accurate,
        # but it will always be accurate when needed for a "cb?" hint.
        
        first_player = players_array[0]
        
        
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
                cb_state["blocker"] = player
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
                if player == first_player:
                    turn += 1
                cb_state["actor"] = player
                cb_state["action"] = action
                cb_state["target"] = target
                cb_state["blocker"] = None


        if my_turn == True and first_player == self.name:
            turn += 1
        
        
        game_dict = {}
        game_dict["players"] = players_dict
        game_dict["turn"] = turn
        game_dict["cb_state"] = cb_state
        return game_dict
        
    def find_target(self, game_dict):
        players_array = list(game_dict["players"].keys())
        random.shuffle(players_array)
        for player in players_array:
            if player == self.name:
                continue
            if game_dict["players"][player]["cards"] != 0:
                target = player
                break
        
        return target
    
    def who_claims_dukes(self):
        players_with_duke = []
        state = 0
        # 0: waiting to see a duke claim
        # 1: waiting to see if the duke claim is challenged
        # Note: if they get challenged, they either lose the duke they had
        #       OR they never had a duke. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["tax", "foreign_aid"]:
                if player not in players_with_duke:
                    players_with_duke.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_duke.remove(player)
                state = 0
        # print(players_with_duke)
        return players_with_duke
    
    def who_claims_assassins(self):
        players_with_assassins = []
        state = 0
        # 0: waiting to see a assassin claim
        # 1: waiting to see if the assassin claim is challenged
        # Note: if they get challenged, they either lose the assassin they had
        #       OR they never had a assassin. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["assassinate"]:
                if player not in players_with_assassins:
                    players_with_assassins.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_assassins.remove(player)
                state = 0
        # print(players_with_assassins)
        return players_with_assassins
    
    def who_claims_captains(self):
        players_with_captains = []
        state = 0
        # 0: waiting to see a captain claim
        # 1: waiting to see if the captain claim is challenged
        # Note: if they get challenged, they either lose the captain they had
        #       OR they never had a captain. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["steal", "block_steal"]:
                if player not in players_with_captains:
                    players_with_captains.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_captains.remove(player)
                state = 0
        # print(players_with_captains)
        return players_with_captains
    
    def who_claims_ambassadors(self):
        players_with_ambassadors = []
        state = 0
        # 0: waiting to see a ambassador claim
        # 1: waiting to see if the ambassador claim is challenged
        # Note: if they get challenged, they either lose the ambassador they had
        #       OR they never had a ambassador. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["exchange", "block_steal"]:
                if player not in players_with_ambassadors:
                    players_with_ambassadors.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_ambassadors.remove(player)
                state = 0
        # print(players_with_ambassadors)
        return players_with_ambassadors
    
    def who_claims_contessas(self):
        players_with_contessas = []
        state = 0
        # 0: waiting to see a contessa claim
        # 1: waiting to see if the contessa claim is challenged
        # Note: if they get challenged, they either lose the contessa they had
        #       OR they never had a contessa. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["block_assassinate"]:
                if player not in players_with_contessas:
                    players_with_contessas.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_contessas.remove(player)
                state = 0
        # print(players_with_contessas)
        return players_with_contessas
    
    def receive(self, message):
        self.log += message
        self.log += "\n"
        if message[:7] == "winner:":
            which_mode = random.randint(0,19)
            if which_mode == 0:
                self.mode = "block"
            elif which_mode == 1:
                self.mode = "challenge"
            else:
                self.mode = "normal"


            game_dict = Couptils.log_to_game_dict(self.log)
            self.memory["games"].append(game_dict)
            
            # Add all the players to memory if they're not already there.
            # and beefier
            
            for player in game_dict["players"].keys():
                if player == self.name:
                    continue
                try:
                    self.memory["opponents"][player]
                except KeyError:
                    self.memory["opponents"][player] = {
                        "challenged" : {},
                        "turn1": {"income":{}, "foreign_aid":{}, "tax":{}, 
                                  "steal":{}, "exchange":{}}
                    }
            
            counter = 0
            
            for turn in game_dict["turns"]:
                counter += 1
                if counter == 1:
                    first_actor = turn["actor"]
                    first_action = turn["action"]
                    if first_actor != self.name:
                        # write turn 1 actions
                        # aka - toa
                        toa = self.memory["opponents"][first_actor]["turn1"]
                        
                        try:
                            toa[first_action]["total"]
                        except:
                            toa[first_action] = {"total": 0}
                        
                        toa[first_action]["total"] += 1
                        #print(toa, toa[first_action])
                if counter == 2:
                    first_actor = turn["actor"]
                    first_action = turn["action"]
                    if first_actor != self.name:
                        # write turn 1 actions
                        # aka - toa
                        toa = self.memory["opponents"][first_actor]["turn1"]
                        
                        try:
                            toa[first_action]["total"]
                        except:
                            toa[first_action] = {"total": 0}
                        
                        toa[first_action]["total"] += 1
                        #print(toa[first_action], toa[first_action]["total"])
                # For all the challenges
                if turn["challenger"] is not None:
                    # who was challenged? The blocker or the actor?
                    if turn["blocker"] is not None:
                        challenged_player = turn["blocker"]
                        challenged_action = "block_"+turn["action"]
                    else:
                        challenged_player = turn["actor"]
                        challenged_action = turn["action"]
                    
                    if challenged_player == self.name:
                        continue # just focus on opponents for now
                    
                    # Now add in the data that the player was challenged doing
                    # this. Add a new category if need be.
                    
                    # pcd: player challenged data
                    pcd = (
                     self.memory["opponents"][challenged_player]["challenged"])
                    
                    try:
                        pcd[challenged_action]
                    except KeyError:
                        pcd[challenged_action] = {
                            "total": 0, # Total times challenged doing this
                            "won": 0    # times won while challenged doing this
                            }
                    
                    pcd[challenged_action]["total"] += 1
                    if turn["challenger_win"] == False: # Challenger lost
                        pcd[challenged_action]["won"] += 1 # Challenged won
                    
            
            
            memory_file = open("Player_Beefiest_memory.pkl", "wb")
            pickle.dump(self.memory, memory_file)
            memory_file.close()
    
    def show(self, show_cards = False):
        print("player", self.name)
        if show_cards:
            print("cards:", self.cards)
        else:
            print("cards:", len(self.cards))
        print("coins:", self.coins)
    
if __name__ == '__main__':
    old_memory = open("Player_Beefiest_memory.pkl", "rb")
    beefier_memory = pickle.load(old_memory)
    old_memory.closed
    
    print(beefier_memory["opponents"])