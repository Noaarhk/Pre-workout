def go_1():
    global k
    for i in range(size):
        if arr[j][i] < 0:
            arr[j][i] = k
            k += 1
    return k

def go_2():
    global k
    for i in range(size):
        if arr[i][size - (1 + j)] < 0:
            arr[i][size - (1 + j)] = k
            k += 1
    return k

def go_3():
    global k
    for i in range(size):
        if arr[size - (1 + j)][size - 1 - i] < 0:
            arr[size - (1 + j)][size - 1 - i] = k
            k += 1
    return k

def go_4():
    global k
    for i in range(size):
        if arr[size - 1 - i][j] < 0:
            arr[size - 1 - i][j] = k
            k += 1
    return k


if __name__ == '__main__':
    size_str, sp_str, direction = input('input the size, the starting point, the direction in order : ').split()
    size = int(size_str)
    sp = int(sp_str)

    arr = [[-1 for _ in range(size)] for _ in range(size)]

    k = 0
    j = 0
    functions = [go_1, go_2, go_3, go_4]


    for j in range(size):
        for t in range(sp - 4, sp):
            k = functions[t]()


    if direction == "C":

        for i in range(size):  # print
            for j in range(size):

                print("%3d" % arr[i][j], end=" ")
            print("")

    elif direction == "CC":
        if sp == 0|2:
            for i in range(size):
                for j in range(size):
                    print("%3d" % arr[j][i], end=" ")
                print("")
        else:
            for i in range(size):
                for j in range(size):
                    print("%3d" % arr[size - 1-j][size - 1 - i], end=" ")
                print("")




