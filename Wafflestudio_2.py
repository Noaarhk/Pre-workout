from copy import deepcopy

if __name__ == '__main__':
    n = 4
    x_i = [[1, -11, -8], [8, -7, 0], [11, -7, 10], [-6, -2, 8]]
    # x = [input("initial coordinates of : ").split() for _ in range(n)]
    a_i = [[0, 0, 0] for _ in range(n)]
    v_i = [[0, 0, 0] for _ in range(n)]
    b = []  # bigger value
    s = []  # smaller value
    sts = []  # 3rd dimension layer # steps
    cnt = 0
    v = []
    x = [[1, -11, -8], [8, -7, 0], [11, -7, 10], [-6, -2, 8]]

    a = []
    #
while True:
    for j in range(3):
        for i in range(n):
            b = []
            s = []
            for k in range(1, n):
                if x_i[i][j] < x_i[i + k - n][j]:
                    b.append(x_i[i + k - n][j])
                elif x_i[i][j] > x_i[i + k - n][j]:
                    s.append(x_i[i + k - n][j])
                elif x_i[i][j] == x_i[i + k - n][j]:
                    pass
            a_i[i][j] = len(b) - len(s)

    for i in range(4):
        for j in range(3):
            v_i[i][j] += a_i[i][j]
            x_i[i][j] += v_i[i][j]

    cnt += 1
    print(cnt)
    if x == x_i:
        break

    # v = [[v[i][j] + a[i][j] for j in range(3)] for i in range(4)]
    #
    # for j in range(n):
    #     for i in range(3):
    #         print(x_i[j][i], end=" ")
    #     print("")

    # x = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
    # # x = [input("initial coordinates of : ").split() for _ in range(n)]
    # a = [[0] for _ in range(n)]
    # v = [[0] for _ in range(n)]
    # b = []  # bigger value
    # s = []  # smaller value
    # #
    # for j in range(3):
    #     for i in range(n):
    #         for k in range(1, n):
    #             if x[i][j] < x[i + k][j]:
    #                 b.append(x[i + k][j])
    #             elif x[i][j] > x[i + k][j]:
    #                 s.append(x[i + k ][j])
    #             elif x[i][j] == x[i + k][j]:
    #                 pass
    #         a[i][j] = len(b) - len(s)
