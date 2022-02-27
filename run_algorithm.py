from time import time


def run_algorithm_on_problem_by_iter_number(problem, search_type, n_iterations, ):
    # Time and count how much out of n_iterations the algorithm succeeded to find a correct solution
    accurate_solution_count = 0
    result_boards = []
    start = time()
    for i in range(n_iterations):
        result = search_type(problem)
        if abs(problem.heuristic(result)) == 0:  # Heuristic = 0 means that we found a correct solution
            accurate_solution_count += 1
            result_boards.append(result)
    end_time = time() - start
    print("Hit rate: %2d/%d\tRuntime: %f" % (accurate_solution_count, n_iterations, end_time))
    if not result_boards:  # if no correct solution was found out of n_iterations
        result_boards.append(result)
    return result_boards, accurate_solution_count / n_iterations, end_time
