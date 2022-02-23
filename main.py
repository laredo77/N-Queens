import random
import time


class Queen:
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
        return

class Board:
    def __init__(self, n=4):
        self.has_conflicts = True
        self.board = []
        self.n = n
        self.queens = []
        self.initialize_board()

    def initialize_board(self):
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            self.board.append(row)

        random_list = list(range(0, self.n))
        random.shuffle(random_list)
        for i in range(len(self.board)):
            random_row = random_list.pop()
            self.board[random_row][i] = 1
            self.queens.append(Queen(random_row, i))

    def heuristic(self, row, col):
        other_row = row - 1
        other_col = col - 1
        m = (col - other_col) / (row - other_row)
        c = col - m * row

        other_row_2 = row - 1
        other_col_2 = col + 1
        m_2 = (col - other_col_2) / (row - other_row_2)
        c_2 = col - m_2 * row

        conflicts_count = 0
        for i in range(self.n):
            if self.queens[i].row == row and self.queens[i].col == col:
                continue
            if self.queens[i].row == row or self.queens[i].col == col:
                conflicts_count += 1
            if self.queens[i].row * m + c == self.queens[i].col:
                conflicts_count += 1
            if self.queens[i].row * m_2 + c_2 == self.queens[i].col:
                conflicts_count += 1
        return conflicts_count / 2

    def heuristic_manager(self):
        self.has_conflicts = False
        for i in range(len(self.queens)):
            if self.heuristic(self.queens[i].row, self.queens[i].col):
                self.has_conflicts = True
                return

    def tabuSearch(self):
        tabu_list = [[0 for _ in range(len(self.board))] for _ in range(len(self.board))]
        iter = 0
        while self.has_conflicts:
            new_queen = random.randint(0, len(self.queens) - 1)
            if self.heuristic(self.queens[new_queen].row, self.queens[new_queen].col) > 0:
                possible_moves = [(i, self.queens[new_queen].col) for i in range(self.n)]
                not_tabu = []
                for i in range(len(possible_moves)):
                    if tabu_list[possible_moves[i][0]][possible_moves[i][1]] <= iter:
                        not_tabu.append(possible_moves[i])
                if len(not_tabu) > 0:
                    min_move = not_tabu[0]
                    min_conflict = self.heuristic(not_tabu[0][0], not_tabu[0][1])
                    for k in range(len(not_tabu)):
                        if min_conflict >= self.heuristic(not_tabu[k][0], not_tabu[k][1]):
                            min_move = not_tabu[k]
                            min_conflict = self.heuristic(not_tabu[k][0], not_tabu[k][1])

                    tabu_list[self.queens[new_queen].row][self.queens[new_queen].col] = iter + (self.n + 10)
                    self.board[self.queens[new_queen].row][self.queens[new_queen].col] = 0
                    self.board[min_move[0]][self.queens[new_queen].col] = 1
                    self.queens[new_queen].row = min_move[0]
                    self.heuristic_manager()
                iter += 1
        # if x == 200: # Max Tabu (constant)
        #     print("LIMIT")
        return

if __name__ == "__main__":
    n = 4
    if n < 4:
        print('Number of queens needs to be above 4')
        exit(0)

    start_time = time.time()
    board = Board(n)
    board.tabuSearch()
    end_time = time.time() - start_time

    for i in range(len(board.board)):
        for j in range(len(board.board)):
            print(board.board[i][j], " ", end="")
        print()
    print()
    print("Execution Time: {:.6f} seconds".format(end_time))
