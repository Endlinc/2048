Task
-----
Model the AI player as a max player, and the computer as a chance player (picking a random open spot to place a 2-tile). Implement a depth-3 game tree and the expectimax algorithm to compute decisions for the AI player. Use the score returned by the game engine as the evaluation function value at the leaf nodes of the depth-3 game trees. 

You can play the game manually using the arrow keys. Pressing 'Enter' will let the AI play, and pressing 'Enter' again will stop the AI player. Read the game engine code from 'game.py' and see how it returns the game state and evaluate its score from an arbitrary game state after an arbitrary player move. 

A depth-3 game tree means the tree should have the following levels: 

- root: player
- level 1: computer 
- level 2: player
- level 3: terminal with payoff (note that we say "terminal" to mean the leaf nodes in the shallow game tree, not the termination of the game itself)

This tree represents all the game states of a player-computer-player sequence (the player makes a move, the computer place a tile, and then the player makes another move, and then evaluate the score). Compute the expectimax values of all the nodes in the game tree, and return the optimal move for the player. In the starter code, the AI just returns a random move.

If you have implemented the AI correctly, you depth-3 search should almost always reach 512 tiles and a score over 5000 quite often, as shown in the movie file. 

Testing
-----
The file 'test\_utils.py' contains code for testing that with the depth-3 tree and the expectimax algorithm, your AI returns the right directions and values on 3 test states. Run the tests using:

$ python main.py -t 1

Notes
------
The following keyboard options are available:
- 'r': restart the game
- 'u': undo a move
- '3'-'7': change board size
- 'g': toggle grayscale
- 'e': switch to extra credit

