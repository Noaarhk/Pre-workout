if __name__ == '__main__':

    xyz = [[1, -11, -8], [8, -7, 0], [11, -7, 10], [-6, -2, 8]]
    xyz_col = [[] for _ in range(3)]  # ABCD의 xyz좌표
    acc_col = [[0 for _ in range(4)] for _ in range(3)]
    vel_col = [[0 for _ in range(4)] for _ in range(3)]
    xyz_col_initial = [[] for _ in range(3)]  # initial value fix
    for i in range(3):
        xyz_col_initial[i] = xyz_col[i][:]

    for j in range(3):  # transpose of xyz
        for i in range(4):
            xyz_col[j].append(xyz[i][j])
    stp = 0
    cnt = [[0] for _ in range(3)]
    while True:
        # step
        for j in range(3):

            b = []
            s = []
            for k in range(1, 4):

                for i in range(4):
                    if xyz_col[j][i - 4] < xyz_col[j][i + k - 4]:
                        b.append(xyz_col[j][i + k - 4])
                    elif xyz_col[j][i] > xyz_col[j][i + k - 4]:
                        s.append(xyz_col[j][i + k - 4])
                    else:
                        pass
                for i in range(4):
                    acc_col[j][i] += len(b) - len(s)
                    vel_col[j] += acc_col[j]
                    xyz_col[j] += vel_col[j]
                    stp += 1

            cnt[j] = stp
            if xyz_col[j] == xyz_col_initial[j] and vel_col[j] == [0, 0, 0]:
                break
