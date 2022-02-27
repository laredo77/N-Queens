# MAIN CLASS
import argparse
from local_search import local_search
from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search
from n_queens import NQueensSearch
from random import choice
from stats_and_plots import generate_graphs


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


def run_algorithms_and_show_boards(board_size_n, iterations_num, is_print_all, ):
    problem = NQueensSearch(board_size_n)
    problems = [problem, problem, problem, problem]
    print("Initial board state:")
    print_board([problem.initial_state()], False)
    for i in range(len(algorithms)):
        print(names[i])
        result_boards, _, _ = local_search(problems[i], algorithms[i], iterations_num, )

        print_board(result_boards, is_print_all)


if __name__ == "__main__":
    desc = "N-queens problem solver by using local search algorithms.\n\t Default arguments: -n=8 ; -i=10 ; --all=0"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-n", type=int, default=8, help="Size of the board")
    parser.add_argument("-i", type=int, default=10, help="Number of iterations")
    parser.add_argument("--all", type=int, dest='all', action='store',
                        choices=range(0, 2), default=0,
                        help="0 = show one solution | 1 = show all solutions")
    args = parser.parse_args()

    n = args.n
    algorithms = [tabu_search, hill_climbing, random_restart, simulated_annealing]
    names = ["Tabu Search", "Hill Climbing", "HC Random Restart", "Simulated Annealing"]

    generate_graphs(algorithms, names)
    #run_algorithms_and_show_boards(n, args.i, args.all)
