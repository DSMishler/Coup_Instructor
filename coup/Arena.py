# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:09:54 2022

@author: Daniel Mishler
"""

import Coup
import Markus
import Trey
import Beef
import JoeyD
import Abe
import Beefiest
import flyswatter
import lazy_sullivan

gm = Coup.Game_Master()

trey = Trey.Player_Trey("trey")
boo = Trey.Player_Trey("boo")
markus = Markus.Player_Markus()
beef = Beef.Player_Beef()
joeyd = JoeyD.Player_JoeyD()
abe = Abe.Player_Abe()
beefiest = Beefiest.Player_Beefiest()
flyswatter = flyswatter.Flyswatter()
sullivan = lazy_sullivan.lsPlayer()


players = [beefiest, sullivan]


wincounts = {}
fname = ""
for player in players:
    wincounts[player.name] = 0
    fname += player.name
wincounts["none"] = 0
fname += ".coup"
for i in range(1000):
    print("game #%d" % i)
    gm.game(players, fname = fname)
    gamefile = open(fname, "r")
    lines = gamefile.read().split('\n')
    winnerline = lines[-2]
    winner = winnerline.split()[1]
    wincounts[winner] += 1

    gamefile.close()


for player in players:
    name = player.name
    print("%s wins %d games" % (name, wincounts[name]))