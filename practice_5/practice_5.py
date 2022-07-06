# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:48:47 2022

@author: Daniel Mishler
"""

# If you haven't finished practices before practice 5, don't worry about it -
# Start here.


# Problem 1
# show with an example whether or not a dictionary is mutable in python


# Build the "Beef" agent, just like how we built Markus in class.
# The agent will be called Player_Beef. Make it in a file called Beef.py
# in your Coup directory.

# Problem 2
# Build Beef's react function for discarding, challenging, and placeback.
# Beef prefers cards in the following priority:
    # duke
    # captain
    # assassin
    # contessa
    # ambassador
# If Beef is challenged, he'll respond to the challenge properly if he can.
# Otherwise, he'll discard the least important card in his hand
# Beef doesn't care if he is holding two of the same card

# Problem 3
# Build Beef's react function for turn.
    # Beef will always take tax on turn 1, no matter what's in his hand
    # Beef will always swap if he has an ambassador,
        # preferring to place back cards so that
        # he will have the highest priority cards
        # If he sees three ambassadors, don't worry about it. He'll just lose
        # that game. If you really played with Beef, he's smarter than this,
        # but Player_Beef is not.
    # Beef will adopt a coup-ing objective if he doesn't have an assassin, and
        # an assassinating objective if he does have one. If he has enough
        # coins to try to pursue his objective, he will.
    # While Beef collects coins, he'll do the following:
        # If he has a Duke, he'll tax
        # else, if he thinks no one else has a Duke, he'll take foreign aid
            # What I mean by this is that your agent will look at the log
            # and see if anyone is both in the game and has claimed to have
            # an unchallenged duke in the past.
                # Note: this part is hard, and I'd recommend doing it after
                # you've finished everything else in the assignment
        # else, he'll income

# Problem 4
# Build Beef's react function for challenging and blocking
    # Beef will always block if he does not have to lie to do it.
    # Beef will never block if he would have to lie to do it.
    # Beef will never challenge, unless it's one of these specific cases:
        # If Beef is holding a Duke, he will challenge a turn 1 tax
        # If Beef is trying to assassinate you and you block, he'll challenge
            # you exactly 50% of the time
        # If Beef is getting assassinated, is holding 1 card, and doesn't
            # have a contessa, he'll challenge


# Problem 5
# Who is more likely to win: Beef or Markus?
# Hint: you need to run many games. Perhaps 1000.
# Automate it
# Run a game, read the winner line, keep a count, and repeat