# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:34:44 2022

@author: Daniel Mishler
"""

"""
What was I thinking when I assigned practice problem 2 to you?

Practice problem 2 took me an hour, which means it likely took many of you
3-4. Not even my solution is fully complete, but it's a primer into how
much there is to think about with a simple problem like parsing for a gamefile.
Every time you go through a large, open-ended exercise like this, your Python
brain is getting smarter. You'll be thinking ahead more, and you'll be much
more prepared for the next time you tackle something like this.

This is the type of learning that I couldn't give you if I just
held you hand through this process. So if you spent
2 or more hours trying this, then you advanced and you achieved what I was
hoping you'd achieve.
"""



# How did I build this file?
# one case at a time. I built it for game_a,
# then game_b
# then game_c
# then game_d
# and so on, making sure it expanded to handle the different cases

# I might not even be done with the game parser yet, but this is the current
# MVP for practice 3
class simple_Player:
    def __init__(self, pname):
        self.name = pname
        self.coins = 2
        self.cards = 2
    def show(self):
        print(self.name)
        print("coins: %d cards: %d" % (self.coins, self.cards))

class GameStatus:
    def __init__(self, playernames):
        self.players = []
        for playername in playernames:
            self.players.append(simple_Player(playername))
        self.active_player = self.players[0]
    def show(self):
        for player in self.players:
            player.show()
    def name_to_player(self, name):
        for player in self.players:
            if name == player.name:
                return player
        return None
    def check_totals(self):
        for player in self.players:
            if player.cards < 0:
                return False
            if player.coins < 0:
                return False
    def who_is_left(self):
        for player in self.players:
            if player.cards > 0:
                return player.name
    def advance_active_player(self):
        ap_index = self.players.index(self.active_player)
        while True:
            ap_index += 1
            if ap_index >= len(self.players):
                ap_index = 0
            if self.players[ap_index].cards > 0:
                self.active_player = self.players[ap_index]
                break
        return


def get_players(line):
    startloc = line.find("[")
    endloc = line.find("]")
    players_string = line[startloc+1 : endloc]
    return players_string.split(", ")

def parse_action(line):
    splitline = line.split()
    actor = splitline[0]
    action = splitline[1]
    if len(splitline) > 2:
        target = splitline[2]
    else:
        target = None
    return [actor, action, target]


global expect_discard # There are other ways to do this and other ways
# to use a global, but this will serve as a good example. This global
# is to determine whether the game should expect a player to discard
# a card next.
def apply_action(gs, line): # apply an action, return false if illegal
    global expect_discard
    [actorname, action, targetname] = parse_action(line)
    actor = gs.name_to_player(actorname)
    target = gs.name_to_player(targetname)
    
    turn_actions = ["tax", "foreign_aid", "income", "steal",
                    "coup", "assassinate", "exchange"]
    
    if action in turn_actions:
        if actor != gs.active_player:
            print("turn order incorrect!")
            return False
    
    if actor.cards == 0 and action != "discard":
        print("acting player is dead!")
        return False
    if action != "discard" and expect_discard == True:
        print("missing the player's discards!")
        return False
    
    
    if action == "steal":
        to_steal = min(2, target.coins)
        actor.coins += to_steal
        target.coins -= to_steal
    elif action == "tax":
        actor.coins += 3
    elif action == "foreign_aid":
        actor.coins += 2
    elif action == "income":
        actor.coins += 1
    elif action == "exchange":
        pass
    elif action == "coup":
        actor.coins -= 7
        target.cards -= 1
        expect_discard = True
    elif action == "assassinate":
        actor.coins -= 3
        target.cards -= 1
        expect_discard = True
    elif action == "discard":
        expect_discard = False
    else:
        print("unknown action '%s'" % action)
        print(line)
        return False
    

    if (gs.check_totals() == False):
        print("incorrect totals!")
        gs.show()
        return False
    
    if action in turn_actions:
        gs.advance_active_player()
    
    return True

def check_winner(gs, line):
    winnername = line.split()[1]
    winnergame = gs.who_is_left()
    if winnername != winnergame:
        print("Error: wrong winner!")
        return False
    # else
    return True

def is_file_legal(fname):
    coupfile = open(fname)
    file_text = coupfile.read()
    file_lines = file_text.split("\n")
    playernames = get_players(file_lines[0])
    gs = GameStatus(playernames)
    
    global expect_discard
    expect_discard = False
    # all but first and last 2 lines (files end in newline)
    for line in file_lines[1:-2]:
        if (apply_action(gs, line) == False):
            return False
    if(check_winner(gs, file_lines[-2]) == False):
        return False
        
    coupfile.close()
    return True


game_names = []
for char in ["a","b","c","d","e","f","g","h"]:
    game_names.append("game_%s.coup" % char)

games_valid = []
for game_name in game_names:
    game_valid = is_file_legal(game_name)
    if game_valid:
        validstr = "valid"
    else:
        validstr = "invalid"
    games_valid.append(validstr)

for (game_name, validstr) in zip(game_names, games_valid):
    print(game_name + ": " + validstr)