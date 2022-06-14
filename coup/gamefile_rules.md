# Coup files

All coup files start with a list of players, in turn order.

In a word with no challenging and blocking, a game file is quite simple.
Each player in turn order must take an action. When a player finally
discards a card, then the gamefile must display who discarded that card.
So, at all times, your game master should know what to expect (when blocks
and challenges get here, it gets more complicated).

The format of a line in the document is the following
```
<Acting_player> <action/reaction> <target>
```
Notice that the target portion is optional. Your program should know
when to expect a target or not. You *can* expect and enforce that
there will be no spaces in player names and action/reaction names.


```
Players: [A, B, C, D]
A tax
B tax
C steal A
D steal C
A assassinate C
C discard contessa
B assassinate D
D discard duke
C tax
D tax
A tax
B tax
C assassinate D
A tax
... # many more lines
A winner
```

Notice that player D was skipped when he was eliminated. Eliminated players
don't get a turn, and they don't get to block or challenge.

This means that, at all times, your program must know
    - How many cards each player has
        - Who is eliminated and must be skipped (or removed from a list...)
    - How many coins each player has
        - What actions are legal for that player
        - If that player must coup


When there is only one player remaining, that player is marked as the winner.
This piece of information is not necessary for the purposes of the game (we
should know who won because we know who the last player is), but it could be
very convenient later on to go through many files with the same players and
just look at the last line to see who won.




(below will be completed before week 4's class)

Add challenging and blocking:

Players: [A, B, C, ...] # Max 6. In turn order.
A tax # First player's action
B challenge A # Other players have a chance to block or challenge
B discard duke # the loser of the challenge discards a card
