def main():
    while 1:
        a=0; b=0; c=0; e=0; f=0; l=""
        try:
            a = str(input("Введите, пожалуйста, число: "))
            c = int(input("Введите, пожалуйста, основание СС, из которой надо перевести: "))
            b = int(input("Введите, пожалуйста, основание СС, в которую надо перевести: "))
        except:
            print("Что-то пошло по пи... не так")
            a = 12
            b = 2
            c = 10
        finally:
            a.upper()
            for i in a:
                f += 1
                if (i == ",")or(i == "."):
                    e = f
            if e:
                f = str(a[(e):len(a):1])
                a = str(a[0:e-1:1])
                if c==10:
                    l = str("." + fldec2n(f, b))
                elif b == 10:
                    l=str("." + fln2dec(f, c))#не работает
                else:
                    l=str("." + fln2n(f, b, c))#не работает
            if c == 10:
                a=int(a)
                print(str(dec2n(a, b))+l)
            elif b == 10:
                print(str(n2dec(a, c))+l)
            else:
                print(str(n2n(a, b, c))+l)


def fldec2n(f: str, b: int) -> str:
    i = 0; d = 0; arr = []; k = ""
    d = int(f)
    l = len(str(d))
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
    b = ""
    ABC = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(10, 16):
        if n == i:
            b = ABC[i - 10]
    if b == "":
        b = str(int(n))
    return b


def buk2n(b: str) -> int:
    n=int(0)
    ABC = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(10,16):
        if b == ABC[i-10]:
            n = int(i)
    if n == 0:
        n=int(b)
    return n


def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    res = power(a * a, n // 2)
    if n % 2:
        res *= a
    return res


def n2n(a: str, b: int, c: int) -> str:
    dec2n(n2dec(a, c), b)


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


def n2dec(a: str, b: int) -> int:
    d = []; c = []; j = ""
    for j in a:
        c += [buk2n(j)]
    c.reverse()
    i = int(0)
    while i < len(c):
        d += [(c[i]) * power(b,i)]
        i+=1
    d.reverse()
    res = 0
    for i in d:
        res += int(i)
    return res


if __name__ == '__main__':
    main()