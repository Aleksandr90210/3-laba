def input_f():
    while True:
        x = int(input('Введите натуральное число'))
        if n > 0:
            break
        print('Неверные даные')
    return x

def x2(x):
    return collatz(x // 2)

def x3_1n(x):
    return collatz(x*3+1)

def collatz(x):
    result = [x]
    if n == 1:
        pass
    elif x % 2 == 0:
        result.extend(x2(n))
    else:
        result.extend(x3_1(n))
    return result

if __name__ == '__main__':
    a = inputs()
    print(collatz(a))
