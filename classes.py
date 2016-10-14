class Complex:
    def __init__(self, realpart, imagpart):
        self.r= realpart
        self.i = imagpart


class MyClass:
    """ A simple example class"""
    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return   'hello world'


class Dog:

    kind = 'canie' # 共有
    # tricks = [] # 共有


    def __init__(self, name):
        self.name = name # インスタンスごと
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == '__main__':
    # x = MyClass()
    # x.data.append('a')
    # print(x.data)

    # x = Complex(3.0, -4.5)
    # print(x.r, x.i)

    x = MyClass()
    #x.counter = 1
    #while x.counter <= 10:
    #    #x.counter = x.counter * 2
    #    x.counter *= 2
    #print(x.counter)
    #del x.counter

    #print(x.f())
    #print(MyClass.f(x))

    #　クラス変数をインスタンス変数
    # x = MyClass()
    # y = MyClass()
    # x.i = 54321
    # print(x.i) # インスタンス変数
    # print(MyClass.i) # クラス変数
    # print(x.data)
    # MyClass.i = 33333
    # print(x.i)  # インスタンス変数
    # print(y.i)  # クラス変数
    # print(MyClass.i)  # クラス変数
    # del x.i
    # print(x.i)

    #  クラス変数とインスタンス変数その２ 65
    d= Dog('Fibo')
    e = Dog('Kurin')
    # print('d.kind:', d.kind) # クラス変数、共有
    # print('e.kind:', e.kind) # クラス変数、共有
    # print('d.name:', d.name) # インスタンス変数、個別
    # print('e.name:', e.name) # インスタンス変数、個別

    d.add_trick('roll over')
    e.add_trick('play dead')
    print(d.tricks)
    print(e.tricks)