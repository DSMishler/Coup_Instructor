#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:47:46 2022

@author: dsmishler
"""

import random
import Couptils
import pickle

### Optimizations to consider
# Go cannon mode less against better known opponents
    # In other words, decide on turn 1 what mode to go into instead of at end
# Count cards
    # Knowing what cards you are holding in hand affects the odds of an
    # opponent lying
# In-game strategy changes
    # A player who loses a block_steal can never block a steal that game
    # A player who takes income on turn 1 probably doesn't have a duke
    # etc...
# Watch for overfitting
    # An agent specifically designed to beat a specific other agent is unlikely
    # to be successful generally
# Tail between legs...
    # If you got challenged doing something and lost, don't do it again.

joeyd_card_priority = [
    "ambassador",
    "assassin",
    "captain",
    "contessa",
    "duke"]

class Player_JoeyD:
    def __init__(self, name="joeyd"):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []
        try:
            memory_file = open("joeyd_memory.pkl", "rb")
            self.memory = pickle.load(memory_file)
            memory_file.close()
        except FileNotFoundError:
            self.memory = {}
            self.memory["games"] = []
            self.memory["opponents"] = {}
        

        self.mode = "normal"
    
    def react(self, hint):
        game_dict = Couptils.log_to_game_dict(self.log)
        if hint == "turn":
            # Can I assassinate or coup?
            target = self.find_active_target(game_dict)

            if "assassin" in self.cards and self.coins >= 3:
                # JoeyD likes to use his assassins, but if he has seen it not
                # work in the past, he won't do it.
                condition_to_assassinate = True
                for turn in game_dict["turns"]:
                    if turn["actor"] == self.name: # It was my turn
                        if turn["action"] == "assassinate": # I assassinated
                            if turn["blocker"] is not None: # Someone blocked
                                if turn["challenger"] is None: #None challenged
                                    condition_to_assassinate = False
                                    break
                if condition_to_assassinate == True:
                    return "assassinate " + target

            
            if self.coins >= 7:
                return "coup " + target
            
            # What's the money-making strategy?
            if "duke" in self.cards:
                return "tax"
            
            
            # If I'm playing like a cannon, let's tax anyway
            if self.mode == "cannon":
                # In a 1v1, record it in my memory
                if len(game_dict["players"].keys()) == 2:
                    for player in game_dict["players"].keys():
                        if player != self.name:
                            other_player = player
                    # pcd: short for player challenges_me data
                    pcd = (self.memory["opponents"]
                                      [other_player]
                                      ["challenges_me"])
                    action = "tax"
                    try:
                        pcd[action]
                    except KeyError:
                        pcd[action] = {
                            "total": 0,
                            "challenged": 0,
                            "lied": 0,
                            "caught": 0
                            }
                    
                    pcd[action]["lied"] += 1
                return "tax"
            
            # Now, even if I'm not playing like a cannon, let's see if I think
            # I can get away with a tax
            if len(game_dict["players"].keys()) == 2:
                for player in game_dict["players"].keys():
                    if player != self.name:
                        other_player = player
                # pcd: short for player challenges_me data
                pcd = (self.memory["opponents"]
                                  [other_player]
                                  ["challenges_me"])
                action = "tax"
                try:
                    pcd[action]
                except KeyError:
                    pcd[action] = {
                        "total": 0,
                        "challenged": 0,
                        "lied": 0,
                        "caught": 0
                        }
                
                # If the other guy catches me less than 1/4 of the time...
                if pcd[action]["caught"] <= pcd[action]["lied"] // 4:
                    pcd[action]["lied"] += 1
                    return "tax"
            if len(game_dict["players"].keys()) > 2:
                # We don't income in FFA, who do you think we are?
                # Note: it's silly to challenge taxes in FFA, but a bot who
                #       does choose to do it will shut JoeyD out of the game
                #       with this choice.
                return "tax"
                    
            return "income"
            
            
        elif hint in ["discard", "placeback"]:
            for consideration in joeyd_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # If we made it here, there's an error
            return "?"
        
        elif hint == "challenged":
            if game_dict["this_turn"]["blocker"] is None:
                action = game_dict["this_turn"]["action"]
            else:
                action = "block_"+game_dict["this_turn"]["action"]
            for card in self.cards:
                if action in Couptils.card_abilities[card]:
                    return card
                
            # If I lost, just discard something according to card probability
            for consideration in joeyd_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
                    
            return "?"
        
        elif hint == "cb?":
            # decide whether to block
            if game_dict["this_turn"]["blocker"] is None:
                action = game_dict["this_turn"]["action"]
                target = game_dict["this_turn"]["target"]
                if action == "steal" and target == self.name:
                    if "captain" in self.cards or "ambassador" in self.cards:
                        return "block"
                if action == "assassinate" and target == self.name:
                    if "contessa" in self.cards:
                        return "block"
                if action == "foreign_aid":
                    if "duke" in self.cards:
                        return "block"
                
                # If JoeyD gets here, he cannot feasibly block this action.
                # If I'm playing like a cannon, sometimes block anyway and see
                # what happens
                if (self.mode == "cannon" and
                  action in Couptils.blockable_actions and
                  (target == self.name or target is None)):
                    if random.randint(1,2) == 1:
                        # In a 1v1, record it in my memory
                        if len(game_dict["players"].keys()) == 2:
                            for player in game_dict["players"].keys():
                                if player != self.name:
                                    other_player = player
                            # pcd: short for player challenges_me data
                            pcd = (self.memory["opponents"]
                                              [other_player]
                                              ["challenges_me"])
                            action = "block_"+action
                            try:
                                pcd[action]
                            except KeyError:
                                pcd[action] = {
                                    "total": 0,
                                    "challenged": 0,
                                    "lied": 0,
                                    "caught": 0
                                    }
                            
                            pcd[action]["lied"] += 1
                            
                        return "block"
                # Else I'm in normal mode. But if I won't get caught blocking,
                # I'll block...
                if (len(game_dict["players"].keys()) == 2 and
                  action in Couptils.blockable_actions and
                  (target == self.name or target is None)):
                    for player in game_dict["players"].keys():
                        if player != self.name:
                            other_player = player
                    # pcd: short for player challenges_me data
                    pcd = (self.memory["opponents"]
                                      [other_player]
                                      ["challenges_me"])
                    action = "block_"+action
                    try:
                        pcd[action]
                    except KeyError:
                        pcd[action] = {
                            "total": 0,
                            "challenged": 0,
                            "lied": 0,
                            "caught": 0
                            }
                    
                    
                    # If the other guy catches me less than 1/4 of the time...
                    if pcd[action]["caught"] <= pcd[action]["lied"] // 4:
                        pcd[action]["lied"] += 1
                        return "block"
                                        
            else:
                action = "block_"+game_dict["this_turn"]["action"]
            
            
            if (self.mode == "cannon" and
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
                shortcut = (self.memory["opponents"]
                                       [actor_in_question]
                                       ["challenged"]
                                       [action_in_question])
                odds_of_truth = shortcut["won"]/shortcut["total"]
                if len(game_dict["players"].keys()) == 2:
                    players_modifier = 1
                elif len(game_dict["players"].keys()) == 3:
                    players_modifier = 0.5
                else:
                    players_modifier = 0.1
                if odds_of_truth <= 0.5 * players_modifier:
                    challenge_it = True
                else:
                    challenge_it = False
            except KeyError:
                challenge_it = False
                # JoeyD has no information to go off of
            if challenge_it == True:
                return "challenge"
            
            
            # Finally, before I pass, I have to ask: should I hail mary?
            if game_dict["this_turn"]["target"] == self.name:
                if game_dict["this_turn"]["action"] == "assassinate":
                    if len(self.cards) == 1:
                        return "block" # Hail-mary block
                    
            return "pass"
        else:
            print("error: unknown hint for reaction!")
            return "?"
    
    # Look at the log, and find a player who is still active for a target
    # Perhaps for stealing, coup-ing, or assassinating
    def find_active_target(self, game_dict):
        players_array = list(game_dict["players"].keys())
        random.shuffle(players_array)
        players_array.remove(self.name)
        target = None # target the player with lowest cards
        for player in players_array:
            if game_dict["players"][player]["cards"] != 0:
                if target is None:
                    target = player
                if (game_dict["players"][player]["cards"] <
                  game_dict["players"][target]["cards"]):
                    target = player
        
        return target
                
    def receive(self, message):
        self.log += message
        self.log += "\n"
        if message[:8] == "players:":          
            # Add all the players to memory if they're not already there.
            game_dict = Couptils.log_to_game_dict(self.log)
            for player in game_dict["players"].keys():
                if player == self.name:
                    continue
                try:
                    self.memory["opponents"][player]
                except KeyError:
                    self.memory["opponents"][player] = {
                        "challenged" : {},
                        "challenges_me" : {},
                        "turn1": {"total": 0}
                    }
            
            if len(game_dict["players"].keys()) == 2:
                cannon_odds = 10
            elif len(game_dict["players"].keys()) == 3:
                cannon_odds = 20
            else:
                cannon_odds = 50
            cannon_roll = random.randint(1,cannon_odds)
            if(cannon_roll == 1):
                self.mode = "cannon"
            else:
                self.mode = "normal"
                
        if message[:7] == "winner:":
            # Do bookkeeping to remember the data from the previous game.
            game_dict = Couptils.log_to_game_dict(self.log)
        
            
            if len(game_dict["players"].keys()) == 2:
                for player in game_dict["players"].keys():
                    if player != self.name:
                        other_player = player
                for turn in game_dict["turns"]:
                    # For everything JoeyD did that could be challenged, and
                    # each other player in the game
                    # Note: this data is only collected for 1v1s
                    if (turn["actor"] == self.name and
                      turn["action"] in Couptils.challengeable_actions):
                        # JoeyD did an action that could be challenged
                        action = turn["action"]
                    elif turn["blocker"] == self.name:
                        action = "block_"+turn["action"]
                    else:
                        continue # nothing of interest this turn
                        
                        
                    # pcd: short for player challenges_me data
                    pcd = (self.memory["opponents"]
                                      [other_player]
                                      ["challenges_me"])
                    try:
                        pcd[action]
                    except KeyError:
                        pcd[action] = {
                            "total": 0,
                            "challenged": 0,
                            "lied": 0,
                            "caught": 0
                            }
                    
                    
                    # Add 1 to the total
                    pcd[action]["total"] += 1
                        
                    # If they challeged, add 1 to the times they challenged
                    if turn["challenger"] == other_player:
                        pcd[action]["challenged"] += 1
                    
                    # If they won, add 1 to the times they caught me
                    if turn["challenger_win"] == True:
                        pcd[action]["caught"] += 1
                    
                        
                    
                
            for turn in game_dict["turns"]:        
                # For all the times an opponent was challenged by anyone
                if turn["challenger"] is not None:
                    # who was challenged? The blocker or the actor?
                    if turn["blocker"] is not None:
                        challenged_player = turn["blocker"]
                        challenged_action = "block_"+turn["action"]
                    else:
                        challenged_player = turn["actor"]
                        challenged_action = turn["action"]
                        
                    # If I, JoeyD, was challenged, ignore it.
                    if challenged_player == self.name:
                        continue
                                        
                    
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
                    
            
            
            memory_file = open("joeyd_memory.pkl", "wb")
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
    memory_file = open("joeyd_memory.pkl", "rb")
    joeyd_memory = pickle.load(memory_file)
    memory_file.close()
    
    print(joeyd_memory["opponents"])