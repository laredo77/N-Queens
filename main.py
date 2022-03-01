# MAIN CLASS
import sys

from run_algorithm import run_algorithm_on_problem_by_iter_number
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

        char_list = map(list, board)
        for line in char_list:
            print(" ".join(line))
    else:
        # print result
        board = []
        for r in iterations_results:
            for c in r:
                line = ['0'] * len(r)
                line[c] = '1'
                board.append(str().join(line))

        char_list = map(list, board)
        for i in range(0, len(char_list)):
            if i % len(char_list[i]) == 0:
                print("\n")

            print(" ".join(char_list[i]))
    print("\n")


def run_algorithms_and_show_boards(board_size_n, iterations_num, is_print_all, ):
    problem = NQueensSearch(board_size_n)
    problems = [problem, problem, problem, problem]
    print("Initial board state:")
    print_board([problem.initial_state()], False)
    for i in range(len(algorithms)):
        print(names[i])
        result_boards, _, _ = run_algorithm_on_problem_by_iter_number(problems[i], algorithms[i], iterations_num, )

        print_board(result_boards, is_print_all)


if __name__ == "__main__":
    algorithms = [tabu_search, hill_climbing, random_restart, simulated_annealing]
    names = ["Tabu Search", "Hill Climbing", "HC Random Restart", "Simulated Annealing"]

    if sys.argv[1] == '1':
        n = int(sys.argv[2])
        iterations_num = abs(int(sys.argv[3]))
        is_print_all_boards = int(sys.argv[4])
        if (n < 1 or n == 2 or n == 3) or is_print_all_boards not in [0, 1]:
            raise "Please provide the correct arguments"
        print('Running all algorithms')
        run_algorithms_and_show_boards(n, iterations_num, is_print_all_boards)
    elif sys.argv[1] == '0':
        generate_graphs(algorithms, names)
    else:
        raise "Please provide the correct arguments"
