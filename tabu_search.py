import random


def tabu_search(problem):
    opt = problem.initial()
    current = problem.initial()
    tabu_list = [problem.initial()]
    max_tabu_size = 300
    while not problem.goal_test(opt):

        current_neighborhood = problem.nearStates(current)
        current = problem.randomNearState(current)
        for neighbor in current_neighborhood:
            if neighbor == current:
                continue
            if neighbor not in tabu_list and problem.heuristic(neighbor) > problem.heuristic(current):
                current = neighbor

        if problem.heuristic(current) > problem.heuristic(opt):
            opt = current

        tabu_list.append(current)
        if len(tabu_list) > max_tabu_size:
            tabu_list.pop(0)
    return opt

