# Amit Twito, Itamar Laredo
def tabu_search(problem):
    # Set the optimum solution and current states as the initial state
    opt = problem.initial_state()
    current = problem.initial_state()
    # Init tabu list with the initial state
    tabu_list = [problem.initial_state()]
    max_tabu_size = 300
    while not problem.is_goal_state(opt):  # Loop until we reach the goal state

        # Choose randomly a neighbor state of the current
        current_neighborhood = problem.get_neighbors(current)
        current = problem.get_random_neighbor(current)

        # Find the minimum neighbor by heuristic function and that is not in the tabu list
        for neighbor in current_neighborhood:
            if neighbor == current:
                continue
            if neighbor not in tabu_list and problem.heuristic(neighbor) > problem.heuristic(current):
                current = neighbor
        # Update the optimal solution
        if problem.heuristic(current) > problem.heuristic(opt):
            opt = current

        # add the current state to the tabu list
        tabu_list.append(current)
        if len(tabu_list) > max_tabu_size:
            tabu_list.pop(0)
    return opt
