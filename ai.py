from __future__ import absolute_import, division, print_function
import copy, random
from math import inf

from game import Game

MOVES = {0: 'up', 1: 'left', 2: 'down', 3: 'right'}
MAX_PLAYER, CHANCE_PLAYER = 0, 1 

# Tree node. To be used to construct a game tree. 
class Node: 
    def __init__(self, state, current_depth, player_type):
        self.state = (copy.deepcopy(state[0]), state[1])

        # to store a list of (direction, node) tuples
        self.children = []

        self.depth = current_depth
        self.player_type = player_type

    # returns whether this is a terminal state (i.e., no children)
    def is_terminal(self):
        #TODO: complete this
        if not self.children:
            return True
        return False

# AI agent. To be used do determine a promising next move.
class AI:
    def __init__(self, root_state, depth):
        self.root = Node(root_state, 0, MAX_PLAYER)
        self.depth = depth
        self.simulator = Game()
        self.simulator.board_size = len(root_state[0])

    # recursive function to build a game tree
    def build_tree(self, node=None):
        if node == None:
            node = self.root

        if node.depth == self.depth: 
            return 

        if node.player_type == MAX_PLAYER:
            # all possible moves (ignore "no-op" moves)

            for direction in MOVES:
                self.simulator.reset(*(node.state))
                if self.simulator.move(direction):
                    child = Node(self.simulator.get_state(), node.depth+1, CHANCE_PLAYER)
                    node.children.append((direction, child))

        elif node.player_type == CHANCE_PLAYER:
            self.simulator.reset(*(node.state))
            for free_title in self.simulator.get_open_tiles():
                self.simulator.tile_matrix[free_title[0]][free_title[1]] = 2
                child = Node(self.simulator.get_state(), node.depth+1, MAX_PLAYER)
                node.children.append((None, child))
                self.simulator.tile_matrix[free_title[0]][free_title[1]] = 0

        for child in node.children:
            self.build_tree(child[1])

    def chance(self, node):
        return 1/len(node.children)

    # expectimax implementation; 
    # returns a (best direction, best value) tuple if node is a MAX_PLAYER
    # and a (None, expected best value) tuple if node is a CHANCE_PLAYER
    def expectimax(self, node = None):
        if node == None:
            node = self.root

        if node.is_terminal():
            return (None, node.state[1])

        elif node.player_type == MAX_PLAYER:
            value = -inf
            direction = 0
            for child in node.children:
                hold = max(value, self.expectimax(child[1])[1])
                if hold > value:
                    value = hold
                    direction = child[0]
            return (direction, value)

        elif node.player_type == CHANCE_PLAYER:
            value = 0
            for child in node.children:
                value = value + self.expectimax(child[1])[1]*self.chance(node)
            return (None, value)

    def compute_decision(self):
        self.build_tree()
        direction, _ = self.expectimax(self.root)
        return direction

    def compute_decision_ec(self):
        return random.randint(0, 3)
