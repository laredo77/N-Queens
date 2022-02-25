from time import time


def local_search(problem, search_type, n_iterations):
    cnt = 0
    start = time()
    s = []
    for i in range(n_iterations):
        result = search_type(problem)
        if abs(problem.heuristic(result)) == 0:
            cnt += 1
            s.append(result)

    print("Hit rate: %2d/%d\tRuntime: %f" % (cnt, n_iterations, time() - start))
    if not s:
        s.append(result)
    return s
