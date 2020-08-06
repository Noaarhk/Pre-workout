if __name__ == '__main__':
    L = 5
    H = 7
    W = 30
    k = 0

    arr = [[k for _ in range(W)] for _ in range(H)]
    # arr = input("input:")

    Length = [arr for _ in range(L)]

    for i in range(H):
        for j in range(W):
            print(arr[i][j], end="")
        print("")

