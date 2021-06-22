import sys
import random

import connect3
from game import Player


class RandomPlayer(Player):

    def __init__(self, state, char):
        super(RandomPlayer, self).__init__(char)
        self.state = state

    def choose_action(self, state):
        if len(state.actions(self.player_char)) > 0:
            return random.choice(state.actions(self.player_char))


class MinimaxPlayer(Player):

    def __init__(self, state, char):
        super(MinimaxPlayer, self).__init__(char)
        self.state = state

    def mini_help(self, state):
        if state.num_empties() == 0:
            return 0
        else:
            if state.winner() == "X":
                return 100
            else:
                return -100

    def choose_action(self, state):
        return self.minimax(state, self.player_char, 3)[1]

    def minimax(self, state, char, depth, best_action=None):

        if depth == 0 or state.game_over():
            if best_action is None:
                best_action = random.choice(state.actions(char))

            if not state.game_over():
                return 0, best_action
            else:
                return self.mini_help(state), best_action

        if char == "X":
            maxEval = -100

            for a in state.actions(char):
                s2 = state.clone()
                s2 = s2.execute(a)
                depth -= 1
                e = self.minimax(s2, "O", depth, best_action)

                if e[0] > maxEval:
                    maxEval = e[0]
                    best_action = a
            return maxEval, best_action

        else:
            minEval = 100

            for a in state.actions(char):
                s2 = state.clone()
                s2 = s2.execute(a)
                depth -= 1
                e = self.minimax(s2, "X", depth, best_action)

                if e[0] < minEval:
                    minEval = e[0]
                    best_action = a
            return minEval, best_action

