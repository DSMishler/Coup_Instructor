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

The player who exchanges will draw two cards from the top of the deck,
then place two cards from their hand on top of the deck. Those cards are
just sitting there, waiting for the next person who exchanges to see what you
just put down.

I anticipate this action prove to be difficult to implement for agents and
players, and it will probably be very difficult for an agent to make good
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
- block\_assassin
- block\_foregin\_aid
- challenge
- discard # Note: also used for inferring the winner of a challenge

The actions marked *like so* require targets. All others do not require targets.

### Are actions case sensitive?

Everything in the Coup gamefile should be lowercase. If you accept that,
I'm happy. If you want to make your gamefile accept uppercase names, that's
fine, but your coup Game\_Master should only output files with all lowercase.

### Should I check to count cards in a game file?

You could, but I'm only going to throw something like that at the advanced
students


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

### What if I echanged, get challenged, and win the challenge?

You place your ambassador in the deck, shuffle the deck, and then proceed
with your exchange.

Note that a failed challenge is the only way the deck ever gets shuffled.

### What if I assassinate a player, he challenges me, and I win?

That player must discard a card for losing the challenge. Then, the assassinate
action resolves. This means the player has discarded 2 cards, and is
immediately eliminated.

## Steals

### Can I steal from a player with fewer than 2 coins?

Yes. Your steal will only take the number of coins that player has
remaining. Possibly zero.
