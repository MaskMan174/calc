def main():
    while 1:
        a=0; b=0; c=0; e=0; f=0; l=""; q=""
        try:
            a = (str(input("Введите, пожалуйста, число: "))).lower()
            c = int(input("Введите, пожалуйста, основание СС, из которой надо перевести: "))
            b = int(input("Введите, пожалуйста, основание СС, в которую надо перевести: "))
        except:
            print("Что-то пошло по пи... не так")
            a="0"
            b=2
            c=10
            raise SystemExit
        finally:
            if a[0] == "-":
                a = a[1:len(a):1]
                q = "-"
            if c == 10:
                for i in a:
                    f += 1
                    if (i == ",")or(i == "."):
                        e = f
                if e:
                    f = str(a[(e): len(a): 1])
                    a = str(a[0: e-1: 1])
                    l = str("." + str(fldec2n(f, b)))
                a=int(a)
                print(q + (str(dec2n(a, b)) + l).upper())
            elif b == 10:
                print(q + str(n2dec(a, c)))
            else:
                print(q + (str(n2n(a, b, c))).upper())


def fldec2n(f: str, b: int) -> str:
    i = 0; d = 0; arr = []; k = ""
    d = int(f)
    l = len(f)
    while d:
        d *= b
        arr += [n2buk(int((d-d%(power(10,l)))/power(10,l)))]
        d = d%(power(10,(l)))
        if len(arr) == 16:
            d=0
    for e in arr:
        k += str(e)
    return k


def n2buk(n: int) -> str:
    if n<10:
        return str(int(n))
    return chr(n+87)


def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    res = power(a * a, n // 2)
    if n % 2:
        res *= a
    return res


def n2n(a: str, b: int, c: int) -> str:
    q = str(n2dec(a, c))
    f=0;e=0
    for i in q:
        f += 1
        if (i == ",")or(i == "."):
            e = f
    f = q[e: len(q): 1]
    q = q[0: e - 1: 1]
    e = fldec2n(f, b)
    f = str(dec2n(int(q), b) + "." + e)
    return f


def dec2n(a: int, b: int) -> str:
    d = []
    i = ''
    while a:
        d += [n2buk(a % b)]
        a = (a - a % b) / b
    d.reverse()
    res = ""
    for i in d:
        res += str(i)
    return res


def n2dec(N: str, a:int) -> float:
    drob = int(0)
    n = 0.0
    for i in range(0, len(N)):
        if N[i] == '.':
            drob = i
    for i in range(0, len(N)):
        if (i < drob):
            n += b2c(N[i]) * pow(a, drob-i-1)
        if (i > drob):
            n += b2c(N[i]) * pow(a, drob-i)
    return n


def b2c(n: str) -> int:
    if (ord(str(n)) > 96):
        n = int(ord(str(n)) - 87)
    return int(n)


if __name__ == '__main__':
    main()