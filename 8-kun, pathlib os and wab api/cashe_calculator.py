from functools import lru_cacheimport syssys.setrecursionlimit(18 ** 4)add = lambda x, y: x + ysub = lambda x, y: x - yinc = lambda x, y: x * ydiv = lambda x, y: x / ymodulus = lambda x, y: x % ydef factorial(n: int) -> int:    res: int = 1    while n:        res *= n        n -= 1        if n == 1:            break    return resdef fibonacci(n):    if n == 0:        return 0    elif n == 1 or n == 2:        return 1    else:        return fibonacci(n - 1) + fibonacci(n - 2)@lru_cache(maxsize=128)def cashed_calculator(n: int) -> int:    try:        if n == 1:            ask_x, ask_y = int(input('Raqam kiriting: ')), int(input('Raqam kiriting: '))            return add(ask_x, ask_y)        elif n == 2:            ask_x, ask_y = int(input('Raqam kiriting: ')), int(input('Raqam kiriting: '))            return sub(ask_x, ask_y)        elif n == 3:            ask_x, ask_y = int(input('Raqam kiriting: ')), int(input('Raqam kiriting: '))            return inc(ask_x, ask_y)        elif n == 4:            ask_x, ask_y = int(input('Raqam kiriting: ')), int(input('Raqam kiriting: '))            return div(ask_x, ask_y)        elif n == 5:            ask_x, ask_y = int(input('Raqam kiriting: ')), int(input('Raqam kiriting: '))            return modulus(ask_x, ask_y)        elif n == 6:            ask_factorial_num = int(input('Factorial uchun raqam kiriting: '))            return factorial(ask_factorial_num)        elif n == 7:            ask_fibonacci_num = int(input('Fibonacci sonlari uchun raqam kiriting: '))            return fibonacci(ask_fibonacci_num)    except:        raise "Siz integer qiymat kiritishingiz kerak"ask_calc = int(input("1. qo'shish\n2. ayirish\n3. ko'paytirish\n4. bo'lish\n5. modulus\n6. factorial\n7. "                     "fibonacci\n\n1 dan 7 gacha raqam kiriting:  "))print(cashed_calculator(ask_calc))