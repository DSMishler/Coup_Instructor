#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:28:06 2022

@author: dsmishler
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []
    
    def react(self, hint):
        if hint == "turn":
            reaction = input("your turn: ")
            while reaction == "show":
                print("your cards: ", self.cards)
                print("your coins: ", self.coins)
                print("so far:")
                print(self.log)
                reaction = input("your turn: ")
            return reaction
        elif hint == "discard":
            reaction = input("discard: ")
            while reaction == "show":
                print("you must discard")
                print("your hand:", self.cards)
                reaction = input("discard: ")
            return reaction
        elif hint == "placeback":
            reaction = input("placeback: ")
            while reaction == "show":
                print("you must placeback from your exchange")
                print("your hand:", self.cards)
                reaction = input("placeback: ")
            return reaction
        elif hint == "challenged":
            reaction = input("challenged: ")
            while reaction == "show":
                print("you must choose a card to respond to the challenge")
                print("your hand:", self.cards)
                reaction = input("challenged: ")
            return reaction
        elif hint == "cb?":
            reaction = input("challenge or block?: ")
            while reaction == "show":
                print("you must choose to challenge, block, or pass.")
                print("your hand:", self.cards)
                reaction = input("challenge or block?: ")
            return reaction
        else:
            print("uknown hint '%s'" % hint)
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
        print(message)

    def show_all(self):
        print("player", self.name)
        print("cards:", self.cards)
        print("coins:", self.coins)


def double_list(mylist):
    orig_len = len(mylist)
    for i in range(orig_len):
        mylist.append(mylist[i])
    return mylist