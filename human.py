import sys
from game import Player
import connect3


class HumanPlayer(Player):

    def __init__(self, player_char, state):
        super(HumanPlayer, self).__init__(player_char)
        self.state = state

    def choose_action(self, state):

        for i in range(len(state.actions(self.player_char))):
            print(str(i) + ":" + " " + str(state.actions(self.player_char)[i]))

        try:
            user_inp = int(input("Please choose an action:\n"))
            return state.actions(self.player_char)[user_inp]
        except IndexError as e:
            print("not quite...enter a valid number\n")
            sys.exit()
        except ValueError as e:
            print("not quite...enter a number\n")
            sys.exit()
