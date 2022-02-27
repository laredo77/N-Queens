from random import shuffle


def hill_climbing(problem):
    current = problem.initial_state()
    while True:
        neighbours = problem.get_neighbors(current)
        if not neighbours:
            break
        # shuffle(neighbours)
        neighbour = max(neighbours, key=lambda state: problem.heuristic(state))
        if problem.heuristic(neighbour) <= problem.heuristic(current):
            break
        current = neighbour
    return current


# HC com random restart
def random_restart(problem, limit=10):
    state = problem.initial_state()
    count = 0
    while problem.is_goal_state(state) == False and count < limit:
        state = hill_climbing(problem)
        count += 1
    return state
