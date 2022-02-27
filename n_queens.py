from random import choice
from collections import Counter
from random import randrange

class SearchProblem:
    def __init__(self, initial=None):
        pass

    def initial_state(self):
        pass

    def is_goal_state(self, state):
        pass

    def heuristic(self, state):
        pass

    def get_neighbors(self, state):
        pass

    def get_random_neighbor(self, state):
        return choice(self.get_neighbors(state))


class NQueensSearch(SearchProblem):

    def __init__(self, N):
        self.N = N

    def initial_state(self):
        return list(randrange(self.N) for _ in range(self.N))

    def is_goal_state(self, state):
        a, b, c = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True

    def heuristic(self, state):
        a, b, c = [Counter() for _ in range(3)]

        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def get_neighbors(self, state):
        near_states = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col
                    near_states.append(list(aux))
        return near_states