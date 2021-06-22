import sys
import random

import connect3
import util


class Player:

    def __init__(self, player_char):
        self.player_char = player_char

    def choose_action(self, state):
        pass


class Game:

    def __init__(self, state, p1, p2):
        self.state = state
        self.p1 = p1
        self.p2 = p2

    def play(self):
        list_states = []
        flag = 1
        list_states.append(self.state.clone())

        while not self.state.game_over():
            a = None

            if flag == 1:
                a = self.p1.choose_action(self.state)
                flag = 2
            else:
                a = self.p2.choose_action(self.state)
                flag = 1

            self.state.execute(a)
            list_states.append(self.state.clone())
            util.pprint(self.state)

        if self.state.num_empties() == 0:
            return None
        else:
            return self.state.winner(), list_states
