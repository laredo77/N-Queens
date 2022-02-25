from random import choice


def printBoard(result, param):
    if not result:
        print([None])
    if param == 0 and result:
        r = choice(result)
        # print r
        board = []
        for col in r:
            line = ['0'] * len(r)
            line[col] = '1'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print(" ".join(line))
    else:
        # print result
        board = []
        for r in result:
            for c in r:
                line = ['0'] * len(r)
                line[c] = '1'
                board.append(str().join(line))

        charlist = map(list, board)
        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print("\n")

            print(" ".join(charlist[i]))
    print("\n")
