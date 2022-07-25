#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:47:46 2022

@author: dsmishler
"""

import random
import Couptils
    

class Player_Abe:
    def __init__(self, name="abe"):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []

    
    def react(self, hint):
        game_dict = Couptils.log_to_game_dict(self.log)
        if hint == "turn":
            # Can I assassinate or coup?
            target = self.find_active_target(game_dict)

            if "assassin" in self.cards:
                if self.coins >= 3:
                    return "assassinate " + target
            
            if self.coins >= 7:
                return "coup " + target
            
            # What's the money-making strategy?
            if "duke" in self.cards:
                return "tax"
            
            return "income"
            
            
        elif hint in ["discard", "placeback"]:
            discard_me = self.cards[0]
            return discard_me
        
        elif hint == "challenged":
            if game_dict["this_turn"]["blocker"] is None:
                action = game_dict["this_turn"]["action"]
            else:
                action = "block_"+game_dict["this_turn"]["action"]
            for card in self.cards:
                if action in Couptils.card_abilities[card]:
                    return card
            return self.cards[0]
        
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
            else:
                action = "block_"+game_dict["this_turn"]["action"]
            
            # never challenge, only block or pass
                
            return "pass"
        else:
            print("error: unknown hint for reaction!")
            return "?"
    
    # Look at the log, and find a player who is still active for a target
    # Perhaps for stealing, coup-ing, or assassinating
    def find_active_target(self, game_dict):
        players_array = list(game_dict["players"].keys())
        random.shuffle(players_array)
        for player in players_array:
            if player == self.name:
                continue
            if game_dict["players"][player]["cards"] != 0:
                target = player
                break
        
        return target
                
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
    
