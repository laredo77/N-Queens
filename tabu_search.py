

def tabu_search(problem):
    opt = problem.initial_state()
    current = problem.initial_state()
    tabu_list = [problem.initial_state()]
    max_tabu_size = 300
    while not problem.is_goal_state(opt):

        current_neighborhood = problem.get_neighbors(current)
        current = problem.get_random_neighbor(current)
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

