# Coup 2022

Daniel Mishler's Python class for those learning Coup Agents in 2022

# Coup FAQ

FAQ that have only been asked by me so far.

## Deck

### What's in my deck?

Place exactly 3 of each in your deck:

- duke
- captain
- assassin
- contessa
- ambassador

### How does ambassador exchange with the deck?

I note that the rules state the ambassador takes cards *randomly* from the
deck, but we will do something special for our version of Coup.

The player who exchanges will draw two cards from the top of the deck,
then place two cards from their hand on top of the deck. Those cards are
just sitting there, waiting for the next person who exchanges to see what you
just put down.

This choice was fun to do when Coup was played with a group of friends
at a lunch table, but it will probably be very difficult
for an agent to make good
use of it.

## Game file

### What are legal actions and reactions, and what are they called?

The legal actions/reactions (inclusive) are:
- income
- foreign\_aid
- *coup*
- tax
- *steal*
- exchange
- *assassinate*
- block\_steal
- block\_assassinate
- block\_foregin\_aid
- challenge

Other things you might see in the gamefile are:
- players: # The first line of the file to tell you who is playing
- discard  # Note: also used for inferring the winner of a challenge
- winner:  # Just for who won the game

The actions marked *like so* require targets. All others do not require targets.

### Are actions case sensitive?

Everything in the Coup gamefile should be *lowercase*. If you accept that,
I'm happy. If you want to make your gamefile accept uppercase names, that's
fine, but your coup Game\_Master should only output files with all lowercase.

### Should I check to count cards in a game file?

You could, but I'm only going to throw something like that at the advanced
students. You can assume that all game files are valid unless something says
otherwise.


## 1v1 Play

### How do we reconcile the going first advantage?

We don't. It's just a huge advantage to go first. Coup suggests giving the
starting player only 1 coin instead of 2, but we will *not* be doing that.
Instead, we will be playing thousands of games and ensuring that going first
is chosen at random. This way, the advantage will even out between two players.

### Do players get to both block and challenge?

No, if a player is faced with an action that they can either block *or*
challenge, they must choose one, not both.

## Group Play

### What if two players each want to simultaneously block/challenge an action?

If a player takes an action, each player is individually (and secretly)
asked whether they want to block or challenge. If two players want to
challenge, say, then one of the two players is chosen at random to be
the challenger. The
player who didn't get selected - no one will even know he tried to challenge.

### What if one player wants to block and one player wants to challenge?

Blocks are handled first. Consider this example

- player A steals from player B
- player C wishes to challenge and player B wishes to block
- player B gets to block, and no one will even know player C would have
  challenged
- Now all players are prompted if they wish to challenge player B's block.

## Challenges

### What can be blocked or challenged

Only the last action or reaction can be blocked or challenged, assuming it
is blockable/challengeable. Nothing before that can be blocked or challenged.

### What happens when a challenge is called

Remember, that as soon as a challenge is called, the challenge is resolved
by the challenged player revealing a card in their hand. If the challenged
player loses, the turn immediately ends. If the challenged player wins,
then the challenging player must discard a card and the challenged player
shuffles his card into the deck and draws a new (possibly the same) card.
Then his action/reaction proceeds without any further interruption.
No more blocks or challenges can happen that turn.

### What if I exchange, get challenged, and win the challenge?

You place your ambassador in the deck, shuffle the deck, and then proceed
with your exchange.

Note that a failed challenge is the only way the deck ever gets shuffled.

### What if I assassinate a player, he challenges me, and I win?

That player must discard a card for losing the challenge. Then, the assassinate
action resolves. This means the player has discarded 2 cards, and is
immediately eliminated.

### What if I assassinate a player, he challenges me, and I lose?

The player you assassinated does not have to discard a card. At the table
in person, if you've played with me, you often notice that we don't give a
refund to the player who did the assassinate. Per the rules, the player
who lost the challenge still gets their money back, and the `Game_Master`
will also treat it this way.

### Do I keep to keep my coins if I assassinate a player and am blocked?

No, you still lose the 3 coins, making the assassin a tricky exception in
action a handling.

## Steals

### Can I steal from a player with fewer than 2 coins?

Yes. Your steal will only take the number of coins that player has
remaining. Possibly zero.

### Do I have to claim how to block a steal with captain or ambassador?

No. If you block a steal and are challenged, you may reveal a captain
*or* an ambassador and you will win the challenge. This may not be the
way that the rules portray blocking of steals, but this is the way *our*
`Game_Master` will handle it.

### What if I steal from someone, but they are eliminated via a challenge?

This could happen if you steal from someone with 1 card and they fail in
a challenge to your steal or if someone succeeds in a challenge to their block.
You would still get the coins you stole.

## My player agent

### How does my player interact with the `Game_Master` class?

Your player can interact with `Game_Master` in a few ways

#### receive()

A method that takes a string as an argument. Every time the game master
writes something to the game log, the game master will also broadcast it to
its players via this method. You ought to store it in a log, and maintain that
information however you want.

#### react()

When your player needs to do something, the game master will communicate via
this method to your player. It will provide a hint as an argument
to your player about what it might want to do:

- "turn": it is your turn and you must choose an action
- "discard": you must discard a card because you lost a challenge or were 
            successfully assassinated or coup-ed
- "placeback": you must place a card back (during an ambassador excahnge)
- "challenged": you must reveal a card from your hand as a result
            of being challenged
- "cb?": someone performed an action that was challengeable or blockable.
         It might be only challengeable, only blockable, or both. You must
         either challenge, block, or pass.

#### show()

It's just a good idea to have a function that shows your player's cards

### How does my player know how to interact with other players?

This 'history' recording will be big for week 6. However, we will be doing it
by managing a file '(playername).player'