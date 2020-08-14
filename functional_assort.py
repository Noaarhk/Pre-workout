from math import gcd
#최대공약수

def transpose(original_matrix, n, m):
    transposed_matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            transposed_matrix[i].append(original_matrix[j][i])
    return transposed_matrix


def update_acc():
    _xyz_acc = [[] for _ in range(3)]
    for j in range(4):
        b = []
        s = []
        for k in range(4):
            if xyz_t[i][j] != xyz_t[i][k]:
                if xyz_t[i][j] < xyz_t[i][k]:
                    b.append(xyz_t[i][k])
                elif xyz_t[i][j] > xyz_t[i][k]:
                    s.append(xyz_t[i][k])
        _xyz_acc[i].append(len(b) - len(s))
    return _xyz_acc


def update_vel():
    for j in range(4):
        xyz_vel[i][j] += xyz_acc[i][j]


def update_loca():
    for j in range(4):
        xyz_t[i][j] += xyz_vel[i][j]


if __name__ == '__main__':
    xyz = [[1, -11, -8], [8, -7, 0], [11, -7, 10], [-6, -2, 8]]
    xyz_t = transpose(xyz, 3, 4)
    xyz_t_initial = [xyz_t[i][:] for i in range(3)]
    xyz_vel = [[0 for _ in range(4)] for _ in range(3)]  # [0000,0000,0000]
    xyz_vel_initial = [[0 for _ in range(4)] for _ in range(3)]

    count = [0, 0, 0]

    for i in range(3):
        while True:
            xyz_acc = update_acc()
            update_vel()
            update_loca()
            count[i] += 1
            if xyz_t[i] == xyz_t_initial[i] and xyz_vel[i] == xyz_vel_initial[i]:
                break

    print(count)
    xy_cycle = count[0] * count[1] // gcd(count[0], count[1])
    xyz_cycle = xy_cycle * count[2] // gcd(xy_cycle, count[2])
    print(xyz_cycle)
