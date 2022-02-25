<<<<<<< HEAD
# MAIN CLASS
import argparse
from print_board import printBoard
from localSearch import localSearch
from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search
from NQueens import NQueensSearch

if __name__ == "__main__":

    # Parametros
    str = "N-queens problem solver by using local search algorithms.\n\t Author: Vitor Veras.\t Default arguments: -n=8 ; -i=10 ; --all=0"
    parser = argparse.ArgumentParser(description=str)
    parser.add_argument("-n", type=int, default=4, help="Size of the board")
    parser.add_argument("-i", type=int, default=10, help="Number of iterations")
    parser.add_argument("--all", type=int, dest='all', action='store',
                        choices=range(0, 2), default=0,
                        help="0 = show one solution | 1 = show all solutions")
    args = parser.parse_args()

    test = localSearch()
    problem = NQueensSearch(args.n)
    algorithms = [tabu_search, hill_climbing, random_restart, simulated_annealing]
    names = ["tabu search", "hill_climbing", "hc_random_restart", "simulated_annealing"]
    problems = [problem, problem, problem, problem]
    for i in range(len(algorithms)):
        print(names[i])
        result_board = test.local_search(problems[i], algorithms[i], args.i)

        printBoard(result_board, args.all)
