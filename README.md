# Coup 2022

Daniel Mishler's Python class for those learning Coup Agents in 2022

# Coup FAQ

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
- winner # Just for the end of the file

The actions marked *like so* require targets. All others do not require targets.

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
