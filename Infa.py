def main():
    while 1:
        a=0; b=0; c=0
        try:
            a = int(input("Введите, пожалуйста, число: "))
            b = int(input("Введите, пожалуйста, основание СС, в которую надо перевести: "))
            c = int(input("Введите, пожалуйста, основание СС, из которой надо перевести: "))
        except:
            print("Что-то пошло по пи... не так")
            a = 12
            b = 2
            c = 10
        finally:
            if c == 10:
                print(dec2n(a, b))
            elif b == 10:
                print(n2dec(a, c))
            else:
                print(n2n(a, b, c))


def dec2n(a: int, b: int) -> int:
    d = []
    i = int(0)
    while a:
        d += [a % b]
        a = (a - a % b) / b
    d.reverse()
    res = 0
    for i in d:
        res *= 10
        res += int(i)
    return res


def n2dec(a: int, b: int) -> int:
    d = []
    i = int(0)
    while a:
        d += [(a % 10) * power(b,i)]
        a -= a%10
    d.reverse()
    res = 0
    for i in d:
        res *= 10
        res += int(i)
    return res


def n2n(a: int, b:int, c:int) -> int:
    dec2n(n2dec(a, c), b)


def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    res = power(a * a, n // 2)
    if n % 2:
        res *= a
    return res


if __name__ == '__main__':
    main()