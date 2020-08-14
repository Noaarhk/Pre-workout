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
#
#
# a = [[0 for _ in range(4)] for _ in range(3)]
# b = [[0] for _ in range(4) for _ in range(3)]
#
# print(a)
# print(b)
# k = 0
#
# def bot():
#     global k
#     for i in range(3):
#         for j in range(4):
#             a[i][j] = k
#             k += 1
# bot()
# print(a)
#
# c = a
# a[0][1] = 10000
# print(c)

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result
#
#
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
#
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#
#
# a = SafeFourCal(4, 0)
#
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())



# print(id(a.first))



# if __name__ == '__main__':
    # class Student:
    #     count = 0
    #     students = []
    #
    #     # @classmethod
    #     # def print(cls):
    #     #     print("----- 학생 목록 -----")
    #     #     print("이름 \t 총점 \t 평균")
    #     #     for student in cls.students:
    #     #         print(str(student))
    #     #     print("----- ----- -----")
    #
    #     def print():
    #         print("----- student list -----")
    #         print("이름 \t 총점 \t 평균")
    #         for student in Student.students:
    #             print(student)
    #         print("----- ----- -----")
    #
    #     def __init__(self, name, korean, math, english, science):
    #         self.name = name
    #         self.korean = korean
    #         self.math = math
    #         self.english = english
    #         self.science = science
    #         Student.count += 1
    #         Student.students.append(self)
    #
    #     def get_sum(self):
    #         return self.korean + self.math + self.english + self.science
    #
    #     def get_average(self):
    #         return self.get_sum() / 4
    #
    #     def __str__(self):
    #         return f"{self.name} \t {self.get_sum()} \t {self.get_average()}"
    #
    #
    # Student("최한결", 10, 123, 14, 15)
    # Student("류남규", 15, 25, 264, 464)
    #
    # Student.print()

#
# class Teacher:
#     name = ""
#     height = 0
#     subject = ""
#
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height
#         pass
#
#     def __str__(self):
#         return f"{self.name} {self.height}"
#
#     def to_string(self):
#         return f"{self.name}"
#
#     def grow_up(self):
#         self.height += 10
#
# if __name__ == '__main__':
#     jotgyu = Teacher("jotgyu",160)
#     print(jotgyu)
#     jotgyu.grow_up()
#     print(jotgyu)
