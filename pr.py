# a = [go_1, go_2, go_3, go_4]
#
# while True:
#     k = int(input()) # 0 < k < 3
#     print([a[t - 4] for t in range(k , k + 4)])
#
# n = 3
#
# b=[]
# for _ in range(n):
#     a = [[-1 for _ in range(n)] for _ in range(n)]
#     b.append(a)
# b[0][0][0]=1
# b[0][1][1]=0
# # #b[layer][Height][width]]
# #
# print (b)
# b = []

# wrong ans # for i in range (n):
# wrong ans #     b[i] = [a[i]]
#
# b.append(a1)
# b.append(a2)
# b.append(a3)
#
# x, y, z = input("The initial coordinates: ").split()
# print("x coordinate", x)
# print('y coordinate', y)
# print('z coordinate', z)

# # print("%02d"%9)


# a = [[3, -1, -1], [1, 3, 3], [-3, 1, -3], [-1, -3, 1]]
# x = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# v = [[0,0,0] for _ in range(4)]
#
# for i in range(4):
#     for j in range(3):
#         v[i][j] += a[i][j]

# print(v)
# print([[a[i][j] + x[i][j] for j in range(3)] for i in range(4)])


a = [[0 for _ in range(4)] for _ in range(3)]
b = [[0] for _ in range(4) for _ in range(3)]

print(a)
print(b)
k = 0

def bot():
    global k
    for i in range(3):
        for j in range(4):
            a[i][j] = k
            k += 1
bot()
print(a)

c = a
a[0][1] = 10000
print(c)
