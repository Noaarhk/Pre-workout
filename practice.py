if __name__ == '__main__':
    #     def add_all(*args):
    #         result = 0
    #         for element in args:
    #             result += element
    #         return result
    #
    # a = add_all(1,2,3,4,5,6)
    # print(a)

    # ##Dictionary
    #     dick = {"name":"좆결","phone":"01020946651","email":"skarb8277@naver.com"}
    #
    #     print( dick["name"])
    #     print(dick.keys())
    #     print(dick.values())
    #     print(dick.items())
    #     print(dick.get('name'))
    #     print(dick.clear())

    # a = 10
    # b = [1,8,7,10,2]
    #
    # print(a in range(5,13))
    # print(a in range(8))
    # print(a in b)
    ##(begin, last)
    # a = [(1,2),(3,4),(5,6)]
    # for (begin,last) in a:
    #     print(begin*last)
    #
    # student_count = int(input())
    # score = []
    #
    # for _ in range(student_count):
    #     score.append(input())
    #
    # print( score)
    #
    # a = [1,2,3,4]
    # # result = []
    # #
    # # for num in a:
    # #     result.append(num%3) 3으로 나눈 나머지
    # result = [num%3 for num in a]
    # print(result)

    # multi input into list
    # multi input into dictionary

    # def my_print(**kwargs):
    #     print(kwargs)
    # my_print(name="noah",major="mechanical engineering")
    #
    # def divide(a,b):
    #     return a//b,a%b
    # result = divide(5,2)
    # q = result[0]
    # r = result[1]
    #
    # result[0] = 1
    # def say_hello(name,me):
    #     if name == me:
    #         return
    #     print(f"hello,{name}")
    # say_hello('bob','hank')
    # say_hello(1,2)
    # def fibonacci(n):
    #     if n <= 1:
    #         return n
    #     else:
    #         return fibonacci(n - 1) + fibonacci(n - 2)
    #
    #
    # def fibonacci2(n):
    #         if n<= 1:
    #             return n
    #         else:
    #             k = [0, 1]
    #             for i in range (2, n+1):
    #                 k.append(k[i - 1] + k[i - 2])
    #             return k[n]
    # while True:
    #     n = int(input('input:'))
    #     ans = fibonacci2(n)
    #     print(ans)
    # result1 = 0
    # result2 = 0
    # def add1(a):
    #     global result1
    #     return a + result1
    # def add2(a):
    #     global result2
    #     return a + result2
    # @class examples
    # class Calculator:
    #     def __init__(self):
    #         self.result = 0
    #
    #     def add(self, num):
    #         self.result += num
    #         return self.result
    #
    # cal1 = Calculator()
    # cal2 = Calculator()
    #
    # print(cal1.add(3))
    #@class examples2
    # class Cat:
    #     name = ""
    #     color = ""
    #
    #     def __init__(self,name, color):
    #         self.name = name
    #         self.color = color
    #
    #     def info(self):
    #         print('the name of this cat is \"',self.name,'\" and the color of it is \"', self.color,'\"')
    #
    # cat_1 = Cat('Navi','black')
    # cat_2 = Cat('Bloo','Blue')
    #
    # cat_1.info()
    # cat_2.info()
    class Moive:
        title = ""
        Director = ""
        genre = ""

