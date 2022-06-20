# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:06:02 2022

@author: Daniel Mishler
"""

# Dear student:
    # Good job on finding this file. You are welcome to look at the file.
    # I won't stop you or punish you for your curiosity.
# Recommendations:
    # Try to do something on your own for 10 mintues before getting ideas from
    # this file.
    # Never copy-paste: it's always beneficial to type the code out yourself
    # word by word
    # Try to guess why I did things the way I did them

import random


coup_actions = [
    "income",
    "foregin_aid",
    "coup",
    "tax",
    "steal",
    "exchange",
    "assassinate",
    "block_steal",
    "block_assassin",
    "block_foregin_aid",
    "challenge"
    ]

class Deck:
    def __init__(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def insert(self, card):
        # That's right, inserting into the top of the deck
        # requires another method!
        self.cards.insert(0, card)
    def show(self):
        print("deck contents:")
        for card in self.cards:
            print(card)
    def draw(self):
        if len(self.cards) == 0:
            print("Error: draw from empty deck")
            return None
        # else
        first_card = self.cards[0]
        self.cards.remove(first_card)
        return first_card
    def shuffle(self):
        random.shuffle(self.cards)
    def coup_cards(self, copies = 3): # helper function for easy initialization
        self.cards = []
        coup_types = ["duke", "captain", "contessa", "ambassador", "assassin"]
        for i in range(copies):
            for card in coup_types:
                self.add(card)
        self.shuffle()

class Player:
    def __init__(self, name):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []
    def act(self):
        if self.coins < 7:
            return "tax"
        else:
            target = self.find_active_target()
            return "coup" + " " + target
    
    def find_active_target(self):
        # Find all the players
        first_log_line = self.log.split('\n')[0]
        start_i = first_log_line.find('[')
        end_i = first_log_line.find(']')
        players_string = first_log_line[start_i+1:end_i]
        players_array = players_string.split(", ")
        # Remove myself
        players_array.remove(self.name)
        
        # You might entertain using a dictionary here: I will just double
        # the list
        for player in players_array:
            players_array.append(player)
        
        # Find the last player that acted
        for line in self.log.split('\n'):
            player = line.split()[0]
            action = line.split()[1]
            if action == "discard":
                players_array.remove(player)
        
        # You don't need to shuffle, but I will
        random.shuffle(players_array)
        
        target = players_array[0]
        return target
                
    def receive(self, message):
        self.log += message
        self.log += "\n"

    def show_all(self):
        print("player", self.name)
        print("cards:", self.cards)
        print("coins:", self.coins)


class Game_Master:
    def __init__(self):
        self.players = []
        self.active_player_names = []
        self.active_player_name = ""
        self.log = ""
        self.deck = Deck()
    def game_init(self, player_names):
        # You can check for duplicate player names if you're worried about
        # people fiddling with the game
        if(len(player_names) < 2):
            print("Error: game must be played with at least 2 players")
        if(len(player_names) > 6):
            print("Error: game must be played with at most 6 players")
        
        for player_name in player_names:
            self.players.append(Player(player_name))
        
        self.deck.coup_cards()
        
        for player in self.players:
            player.coins = 2
            player.cards = [self.deck.draw(), self.deck.draw()]
                
        self.broadcast("players: " + str(player_names))
        self.active_player_names = player_names.copy()
        self.active_player_name = self.active_players[0]
        # Don't know what .copy() does?
        # TL;DR - you probably don't need it, *but*
        # active_players is a mutable, meaning that it's a special kind of
        # variable that *does* remember what it was set to a while ago
        # if a = b + c, then you change c, a will not change. But if the
        # variable a was a mutable, then a *would* change. This .copy()
        # makes active_players not behave like a mutable.

    def turn(self):
        active_player = self.name_to_player(self.active_player_name)
        action = active_player.act()
        message = self.active_player_name + " " + action
        self.broadcast(message)
        # Next week we have to insert challenge and block architecture here
        # TODO: left off here

        return
    
    def show_all(self):
        print("Coup game")
        print("players:", len(self.players))
        for player in self.players:
            player.show_all()
            print()

    def receive(self, message):
        self.log += message
        self.log += "\n"
    
    def broadcast(self, message):
        self.receive(message)
        for player in self.players:
            player.receive(message)
    
    def name_to_player(self, playername):
        for player in self.players:
            if player.name == playername:
                return player
        # if not found
        print("Error: player '%s' not found" % playername)
        return None

common_players = ["trey", "boo"]
gm = Game_Master()
gm.game_init(common_players)