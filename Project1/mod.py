s = "Hacktiv8-PTP Python for DS"
a = [100, 200, 300]
X = ['Saya', 'Anda']

def foo(arg):
    print(f'arg = {arg}')
    print('arg_lain = {}'.format(arg))
    # print(Y)
    __contoh__(arg)
    __contoh2(arg)

def __contoh__(arg):
    print('Multiply = ', arg*arg)

def __contoh2(arg):
    print('Divide = ', arg/2)
    
class Foo2:
    pass

if __name__ == '__main__':
    print(s)
    print(a)
    foo(100)
    y = Foo2()
    print(y)