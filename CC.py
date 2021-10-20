def main():
    while 1:
        try:
            act = str(input("Если надо перевести из одной СС в другую введите: Перевести\nЕсли надо посчитать числа введите: Счет \n"))
        except:
            print("Что-то пошло по пи... не так")
            act="" #нужно, чтобы не выдало ошибку
            return 0 #чтобы завершить работу
        finally:
            act = act.lower()
            if act == "перевести":
                perev()
            if act == "счет":
                calc()


def calc():
    oper=""
    try:
        ch1 = str(input("Введите первое число "))
        ss1 = int(input("Введите СС первого числа "))
        ch2 = str(input("Введите второе число "))
        ss2 = int(input("Введите СС второго числа "))
        oper = str(input("Введите знак операции "))
        ssres = int(input("Введите СС результата "))
    except:
        print("Что-то пошло по пи... не так")
        ch1="0";ch2="0";ss1=10;ss2=10 #нужно, чтобы не выдало ошибку
        return 0 #чтобы завершить работу
    finally:
        ch1 = ch1.lower()
        ch2 = ch2.lower()
        resdec = float(0); res = ""
        for i in ch1:
            if i == ",":
                i = "."
        for i in ch2:
            if i == ",":
                i = "."
        if ss1!=10:
            ch1 = float(n2dec(ch1, ss1))
        else:
            ch1 = float(ch1)
        if ss2!=10:
            ch2 = float(n2dec(ch2, ss2))
        else:
            ch2 = float(ch2)
        if oper == "+":
            resdec = ch1 + ch2
        elif oper == "-":
            resdec = ch1 - ch2
        elif oper == "*":
            resdec = ch1 * ch2
        elif oper == "/":
            resdec = ch1 / ch2
        else:
            print("Что-то пошло по пи... не так")
            return 0
        res = (n2n(str(resdec), ssres, 10)).upper()
        print(res)


def perev():
    e=0; f=0; l=""; q=""
    try:
        a = (str(input("Введите, пожалуйста, число: "))).lower()
        c = int(input("Введите, пожалуйста, основание СС, из которой надо перевести: "))
        b = int(input("Введите, пожалуйста, основание СС, в которую надо перевести: "))
    except:
        print("Что-то пошло по пи... не так")
        a="0";b=0;c=0 #нужно, чтобы не выдало ошибку
        return 0 #чтобы завершить работу
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
    f=0;e=0;drob=''
    for i in q:
        f += 1
        if (i == ",")or(i == "."):
            e = f
    f = q[e: len(q): 1]
    q = q[0: e - 1: 1]
    drob = fldec2n(f, b)
    if drob != '':
        drob = "." + drob
    f = str(dec2n(int(q), b) + drob)
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
    n = float(0)
    for i in range(len(N)):
        if (N[i] == '.')or(N[i] == ','):
            drob = i
    for i in range(len(N)):
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
