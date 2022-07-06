# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:09:54 2022

@author: Daniel Mishler
"""

import Coup
import Markus
import Trey

gm = Coup.Game_Master()

trey = Trey.Player_Trey("trey")
boo = Trey.Player_Trey("boo")
markus = Markus.Player_Markus()

wincounts_markus = 0
wincounts_trey = 0
wincounts_boo = 0
for i in range(500):
    gm.game([trey, boo, markus], fname = "treyvmarkus.coup")
    gamefile = open("treyvmarkus.coup")
    lines = gamefile.read().split('\n')
    winnerline = lines[-2]
    winner = winnerline.split()[1]
    if winner == "markus":
        wincounts_markus += 1
    elif winner == "trey":
        wincounts_trey += 1
    elif winner == "boo":
        wincounts_boo += 1
    gamefile.close()
    
print("markus wins", wincounts_markus, "games")
print("trey wins", wincounts_trey, "games")
print("boo wins", wincounts_boo, "games")