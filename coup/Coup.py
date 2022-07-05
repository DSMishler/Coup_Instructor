# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:06:02 2022

@author: Daniel Mishler
"""

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
    "foreign_aid",
    "coup",
    "tax",
    "steal",
    "exchange",
    "assassinate",
    "block_steal",
    "block_assassinate",
    "block_foreign_aid",
    "challenge"
    ]

respondable_actions = [
    "foreign_aid",
    "tax",
    "steal",
    "exchange",
    "assassinate",
    "block_steal",
    "block_assassinate",
    "block_foreign_aid",
    ]

card_abilities = {
    "duke" :       ["tax", "block_foreign_aid"],
    "captain" :    ["steal", "block_steal"],
    "assassin" :   ["assassinate"],
    "contessa" :   ["block_assassinate"],
    "ambassador" : ["exchange", "block_steal"]
    }

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
    def turn(self):
        if self.coins < 7:
            return "tax"
        else:
            target = self.find_active_target()
            return "coup" + " " + target
    
    def react(self, hint):
        if hint == "turn":
            return self.turn()
        elif hint in ["discard", "placeback", "challenged"]:
            discard_me = self.cards[0]
            return discard_me
        elif hint == "cb?":
            return "pass"
        else:
            print("error: unknown hint for reaction!")
            return "?"
        
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

    def show(self, show_cards = False):
        print("player", self.name)
        if show_cards:
            print("cards:", self.cards)
        else:
            print("cards:", len(self.cards))
        print("coins:", self.coins)
    

class Game_Master:
    def __init__(self):
        self.players = []
        self.active_player_names = []
        self.active_player_name = ""
        self.log = ""
        self.deck = Deck()
    def game_init(self, players):
        # You can check for duplicate player names if you're worried about
        # people fiddling with the game
        if(len(players) < 2):
            print("Error: game must be played with at least 2 players")
        if(len(players) > 6):
            print("Error: game must be played with at most 6 players")

        self.active_player_names = []
        for player in players:
            self.active_player_names.append(player.name)
            self.players.append(player)
        
        self.deck.coup_cards()
        
        self.log = ""
        for player in self.players:
            player.coins = 2
            player.log = ""
            player.cards = [self.deck.draw(), self.deck.draw()]
        
        first_message = "players: "
        first_message += str(self.active_player_names)
        first_message = first_message.replace("'","")
        
        self.broadcast(first_message)
        self.active_player_name = self.active_player_names[0]


    def turn(self):
        active_player = self.name_to_player(self.active_player_name)
        action = active_player.react("turn")
        message = self.active_player_name + " " + action
        self.broadcast(message)

        
        
        split_action = action.split()
        if len(split_action) == 2:
            action = split_action[0]
            target_name = split_action[1]
        elif len(split_action) == 1:
            target_name = None
        else:
            print("Error: invalid action returned")
        
        # TODO: Check if action was legal
        
        # There are 4 possibilities below:
            # 1 - the action is not blocked and not challenged
            # 2 - the action is not blocked and challenged
            # 3 - the action is blocked and the block is not challenged
            # 4 - the action is blocked and the block is challenged
        challenged = False # successfully challenged
        blocked = False # attempted to be blocked
        if action in respondable_actions:
            reactions = self.get_table_reactions(self.active_player_name)
            # first, see if someone wanted to block. Blocking takes precedence
            # over challenging.
            # TODO: Check if block was legal
            blockers = self.get_players_who("block", reactions)
            if len(blockers) == 0:
                blocked = False
            else:
                random.shuffle(blockers)
                blocker = blockers[0] # pick a blocker at random
                blocking_action = "block" + "_" + action
                message = blocker + " " + blocking_action
                self.broadcast(message)
                reactions = self.get_table_reactions(blocker)
                blocked = True
                # if someone blocked the first time, then anyone who wanted
                # to challenge the first time is ignored. They are given the
                # chance to see if they want to challenge the block instead
            
            challenged = False # set to true if successful
            challengers = self.get_players_who("challenge", reactions)
            if len(challengers) == 0:
                pass
            else:
                random.shuffle(challengers)
                challenger = challengers[0]
                message = challenger + " " + "challenge"
                self.broadcast(message)
                # Now ask the challenged player to reveal a card in their hand
                if blocked == True:
                    challenged_player_name = blocker
                    challenged_action = blocking_action
                else: # blocked == False:
                    challenged_player_name = self.active_player_name
                    challenged_action = action
                challenged_player = self.name_to_player(challenged_player_name)
                shown_card = challenged_player.react("challenged")
                challenged_player.cards.remove(shown_card)
                if challenged_action in card_abilities[shown_card]:
                    # Then the challenger loses, challenged wins
                    self.deck.insert(shown_card)
                    self.deck.shuffle()
                    challenged_player.cards.append(self.deck.draw())
                    challenging_player = self.name_to_player(challenger)
                    discarded_card = challenging_player.react("discard")
                    challenging_player.cards.remove(discarded_card)
                    message = challenger + " discard " + discarded_card
                    if len(challenging_player.cards) == 0:
                        self.eliminate(challenger)
                else:
                    # challenger wins, challenged loses
                    challenged = True
                    message = challenged_player_name + " discard " + shown_card
                    if len(challenged_player.cards) == 0:
                        self.eliminate(challenged_player_name)
                self.broadcast(message)
        
        if (blocked ^ challenged):
            # blocked but not successfully challenged
            # or not blocked but successfully challenged
            pass
        else:
            # not blocked or successfully challenged
            # or blocked but the block was successfully challenged
            self.handle_action(self.active_player_name, action, target_name)


        # Now advance the active player
        self.advance_active_player()

        return


    def show(self, show_cards = False):
        print("Coup game")
        print("players:", len(self.players))
        for player in self.players:
            player.show(show_cards)
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

    def get_table_reactions(self, player_to_exclude=None):
        players_to_ask = self.active_player_names.copy()
        if player_to_exclude is not None:
            players_to_ask.remove(player_to_exclude)
        reactions = []
        for player_name in players_to_ask:
            player = self.name_to_player(player_name)
            reaction = player.react("cb?")
            reactions.append(player_name + " " + reaction)
        return reactions

    def get_players_who(self, response, reactions_list):
        players_responding = []
        for reaction in reactions_list:
            player_name = reaction.split()[0]
            player_response = reaction.split()[1]
            if player_response == response:
                players_responding.append(player_name)
        return players_responding

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


    def game(self, players, fname = "coup_game_test.coup"):
        self.game_init(players)
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



humanPlayer = human_player.Player("me")
trey = Player("trey")
boo = Player("boo")


common_players = [trey, boo]
gm = Game_Master()
# gm.game(common_players)

me_players = [humanPlayer, trey]
gm.game(me_players)