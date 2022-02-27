from numpy import *
import math
import matplotlib.pyplot as plt
from run_algorithm import run_algorithm_on_problem_by_iter_number
from n_queens import NQueensSearch
import plotly.express as px

DEFAULT_BOARD_SIZE = 8
DEFAULT_ITER_NUM = 10


def generate_graphs(algorithms, algorithm_names):
    colors = ['b', 'r', 'g', 'black']
    algo_and_names_zip = list(zip(algorithms, algorithm_names))
    algo_and_colors_zip = list(zip(algorithm_names, colors))

    generate_time_and_iterations_num_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names)
    generate_time_and_board_size_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names, )
    generate_accuracy_and_board_size_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names)
    generate_avg_accuracy_historgram(algo_and_names_zip, algorithm_names, colors)


def generate_avg_accuracy_historgram(algo_and_names_zip, algorithm_names, colors, ):
    avgs = []
    hit_rates_dic_by_alg = {algorithm_name: [] for algorithm_name in algorithm_names}
    iters = 100
    local_search_iters = 20
    for _ in range(iters):
        problem = NQueensSearch(DEFAULT_BOARD_SIZE)
        problems = [problem, problem, problem, problem]
        for i, (algorithm, algorithm_name) in enumerate(algo_and_names_zip):
            _, hit_rate, _ = run_algorithm_on_problem_by_iter_number(problem=problems[i], search_type=algorithm,
                                                                     n_iterations=local_search_iters, )
            hit_rates_dic_by_alg[algorithm_name].append(hit_rate)
    for alg in algorithm_names:
        avg = sum(hit_rates_dic_by_alg[alg]) / iters
        avgs.append(avg)
    fig = px.bar(x=algorithm_names, y=avgs, color=colors)
    fig.update_xaxes(type='category')
    fig.show()


def generate_accuracy_and_board_size_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names, ):
    board_sizes = [i for i in range(4, 28)]
    hit_rate_dic_by_alg = {algorithm_name: [] for algorithm_name in algorithm_names}
    for board_size in board_sizes:
        problem = NQueensSearch(board_size)
        problems = [problem, problem, problem, problem]
        for i, (algorithm, algorithm_name) in enumerate(algo_and_names_zip):
            _, hit_rate, _ = run_algorithm_on_problem_by_iter_number(problem=problems[i], search_type=algorithm,
                                                                     n_iterations=DEFAULT_ITER_NUM, )
            hit_rate_dic_by_alg[algorithm_name].append(hit_rate)
    for alg, color in algo_and_colors_zip:
        plt.plot(board_sizes, hit_rate_dic_by_alg[alg], color, label=alg)
    plt.ylabel('Accuracy')
    plt.xlabel('Board Size')
    plt.title('N-Queens Algorithms Comparison')
    plt.legend()
    plt.savefig('graphs/accuracy_and_sizes_graph.png')
    plt.cla()


def generate_time_and_board_size_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names, ):
    board_sizes = [i for i in range(4, 28)]
    times_dic_by_alg = {algorithm_name: [] for algorithm_name in algorithm_names}
    for board_size in board_sizes:
        problem = NQueensSearch(board_size)
        problems = [problem, problem, problem, problem]
        for i, (algorithm, algorithm_name) in enumerate(algo_and_names_zip):
            _, _, time = run_algorithm_on_problem_by_iter_number(problem=problems[i], search_type=algorithm,
                                                                 n_iterations=DEFAULT_ITER_NUM, )
            times_dic_by_alg[algorithm_name].append(time)
    for alg, color in algo_and_colors_zip:
        plt.plot(board_sizes, times_dic_by_alg[alg], color, label=alg)
    plt.ylabel('Time')
    plt.xlabel('Board Size')
    plt.title('N-Queens Algorithms Comparison')
    plt.legend()
    plt.savefig('graphs/times_and_sizes_graph.png')
    plt.cla()


def generate_time_and_iterations_num_graph(algo_and_colors_zip, algo_and_names_zip, algorithm_names,
                                           ):
    iterations_numbers = [10 * i for i in range(1, 26)]
    times_dic_by_alg = {algorithm_name: [] for algorithm_name in algorithm_names}
    for iterations_num in iterations_numbers:
        problem = NQueensSearch(DEFAULT_BOARD_SIZE)
        problems = [problem, problem, problem, problem]
        for i, (algorithm, algorithm_name) in enumerate(algo_and_names_zip):
            _, _, time = run_algorithm_on_problem_by_iter_number(problem=problems[i], search_type=algorithm,
                                                                 n_iterations=iterations_num)
            times_dic_by_alg[algorithm_name].append(time)
    for alg, color in algo_and_colors_zip:
        plt.plot(iterations_numbers, times_dic_by_alg[alg], color, label=alg)
    plt.ylabel('Time')
    plt.xlabel('Iterations')
    plt.title('N-Queens Algorithms Comparison')
    plt.legend()
    plt.savefig('graphs/times_and_iterations_graph.png')
    plt.cla()
