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
import human_player

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
    
    def react(self, hint):
        if hint == "discard":
            discard_me = self.cards[0]
            return discard_me
        
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
        players_array = double_list(players_array)
        
        # Find the last player that acted
        for line in self.log.split('\n'):
            if line == "":
                continue # ignore the last (empty) line
                # the difference between break and continue here is simply
                # that continue will end the iteration of the for loop, and
                # instead of being *guaranteed* to exit the for loop, will
                # enter the next iteration if there is one to do.
            player = line.split()[0]
            action = line.split()[1]
            if action == "discard" and player != self.name:
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
    
    def show_limited(self):
        print("player", self.name)
        print("cards:", len(self.cards))
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
            if player_name == "me":
                self.players.append(human_player.Player(player_name))
            else:
                self.players.append(Player(player_name))
        
        self.deck.coup_cards()
        
        self.log = ""
        for player in self.players:
            player.coins = 2
            player.log = ""
            player.cards = [self.deck.draw(), self.deck.draw()]
        
        first_message = "players: "
        first_message += str(player_names)
        first_message = first_message.replace("'","")
        
        self.broadcast(first_message)
        self.active_player_names = player_names.copy()
        self.active_player_name = self.active_player_names[0]
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
        
        split_action = action.split()
        if len(split_action) == 2:
            action = split_action[0]
            target_name = split_action[1]
        elif len(split_action) == 1:
            target_name = None
        else:
            print("Error: invalid action returned")
        
        self.handle_action(self.active_player_name, action, target_name)


        # Now advance the active player
        self.advance_active_player()

        return


    def show(self, show_cards = False):
        print("Coup game")
        print("players:", len(self.players))
        for player in self.players:
            if show_cards:
                player.show_all()
            else:
                player.show_limited()
            print()
        print("game so far:")
        print(self.log)

    def receive(self, message):
        self.log += message
        self.log += "\n"
    
    def broadcast(self, message):
        self.receive(message)
        for player in self.players:
            player.receive(message)
    
    def name_to_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        # if not found
        print("Error: player '%s' not found" % player_name)
        return None

    def eliminate(self, player_name):
        self.active_player_names.remove(player_name)
    
    def player_eliminated(self, player_name):
        if player_name in self.active_player_names:
            return False
        else:
            return True
    
    def player_alive(self, player_name):
        if player_name in self.active_player_names:
            return True
        else:
            return False
        
    def advance_active_player(self):
        # note to students: there are *lots* of better ways to do this and
        # I encourage you to take them up
        ap_index = self.active_player_names.index(self.active_player_name)
        ap_index += 1
        if ap_index == len(self.active_player_names):
            ap_index = 0
        self.active_player_name = self.active_player_names[ap_index]

    def handle_action(self, player_name, action, target_name):
        # Handle an unblocked, unchallenged action
        player = self.name_to_player(player_name)
        if target_name is not None:
            target = self.name_to_player(target_name)
        
        if action == "income":
            player.coins += 1
        elif action == "foreign_aid":
            player.coins += 2
        elif action == "tax":
            player.coins += 3
        elif action == "steal":
            coins_to_steal = min(target.coins, 2)
            player.coins += coins_to_steal
            target.coins -= coins_to_steal
        elif action == "coup":
            player.coins -= 7
            if self.player_alive(target.name):
                discarded_card = target.react("discard")
                message = target_name + " discard " + discarded_card
                target.cards.remove(discarded_card)
                self.broadcast(message)
                if len(target.cards) == 0:
                    self.eliminate(target.name)
        elif action == "assassinate":
            player.coins -= 3
            if self.player_alive(target.name):
                discarded_card = target.react("discard")
                message = target_name + " discard " + discarded_card
                target.cards.remove(discarded_card)
                self.broadcast(message)
                if len(target.cards) == 0:
                    self.eliminate(target.name)
        elif action == "exchange":
            player.cards.append(self.deck.draw())
            player.cards.append(self.deck.draw())
            
            for i in range(2):
                placeback_card = player.react("placeback")
                # no message here to broadcast: this information is private
                player.cards.remove(placeback_card)
                self.deck.insert(placeback_card)

        else:
            print("action not implemented:", player_name, action, target)


    def game(self, player_names, fname = "coup_game_test.coup"):
        self.game_init(player_names)
        while len(self.active_player_names) > 1:
            self.turn()
        message = "winner: " + self.active_player_name
        self.broadcast(message)
        gamefile = open(fname, "w")
        gamefile.write(self.log)
        gamefile.close()
        
        
        


# as an aside, I know that `mylist` is a mutable, but I'm returning by value
# anyway to sweep that under the rug
def double_list(mylist):
    orig_len = len(mylist)
    for i in range(orig_len):
        mylist.append(mylist[i])
    return mylist



common_players = ["trey", "boo"]
gm = Game_Master()
gm.game(common_players)