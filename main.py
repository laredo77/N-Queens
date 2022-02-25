# MAIN CLASS
import argparse
from local_search import local_search
from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search
from n_queens import NQueensSearch
from random import choice


def print_board(iterations_results, param):
    if not iterations_results:
        print([None])
    if param == 0 and iterations_results:
        r = choice(iterations_results)
        # print r
        board = []
        for col in r:
            line = ['0'] * len(r)
            line[col] = '1'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print(" ".join(line))
    else:
        # print result
        board = []
        for r in iterations_results:
            for c in r:
                line = ['0'] * len(r)
                line[c] = '1'
                board.append(str().join(line))

        charlist = map(list, board)
        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print("\n")

            print(" ".join(charlist[i]))
    print("\n")


if __name__ == "__main__":

    # Parametros
    desc = "N-queens problem solver by using local search algorithms.\n\t Default arguments: -n=8 ; -i=10 ; --all=0"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-n", type=int, default=4, help="Size of the board")
    parser.add_argument("-i", type=int, default=10, help="Number of iterations")
    parser.add_argument("--all", type=int, dest='all', action='store',
                        choices=range(0, 2), default=0,
                        help="0 = show one solution | 1 = show all solutions")
    args = parser.parse_args()

    problem = NQueensSearch(args.n)
    algorithms = [tabu_search, hill_climbing, random_restart, simulated_annealing]
    names = ["tabu search", "hill_climbing", "hc_random_restart", "simulated_annealing"]
    problems = [problem, problem, problem, problem]
    for i in range(len(algorithms)):
        print(names[i])
        result_board = local_search(problems[i], algorithms[i], args.i)

        print_board(result_board, args.all)
