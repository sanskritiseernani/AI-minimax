import sys
import random

import connect3
import util
import game
import agent
import human

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Argument Error!\n")
        sys.exit()

    list_chars = ["X", "O"]
    list_players = [sys.argv[1], sys.argv[2]]
    ps = []

    state = connect3.State()

    for i in range(2):
        if list_players[i] == "human":
            ps.append(human.HumanPlayer(list_chars[i], state))
        elif list_players[i] == "random":
            ps.append(agent.RandomPlayer(state, list_chars[i]))
        elif list_players[i] == "minimax":
            ps.append(agent.MinimaxPlayer(state, list_chars[i]))
        else:
            print("argument error")
            sys.exit()

    my_game = game.Game(state, ps[0], ps[1])

    try:
        result = my_game.play()
    except AttributeError as e:
        print("Looks like there was a little error!")
        sys.exit()

    if result is None:
        print("It's a TIE!\n")
    else:
        i = list_chars.index(result[0])
        print("The winner is " + str(list_players[i]) + " " + str(list_chars[i]))
        util.pprint(result[1])

