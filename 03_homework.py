def zad6():
    
    maxv = 130 ; v = int(input("Podaj prędkość "))
    
    if v > maxv:
        print("za szybko")
    else:
        print("nie za szybko")


def zad7():
    
    x = int(input("podaj liczbe: "))

    if x % 2 == 0:
        return "even"
    else:
        return "not even"


def zad8():
    
    paul = 21; annie = 18; adult_age = 18;

    if paul >= adult_age and annie >= adult_age:
    
        print("oboje są dorośli")


def zad9():

    a = int(input("podaj liczbe 1: "))
    b = int(input("podaj liczbe 2: "))
    
    if a % 2 == 0 or b % 2 == 0:
        
        print("przynajmniej jedna parzysta ")


def zad10():

    for i in range(5):
        print("practice makes perfect")


def zad11():
    
    for a in range(1, 21):
        print(a)

        
def zad12():

    i = 0
    for a in range(100,150):
        i = i + a 

    print(i)


def zad13():
    
    for a in range(1, 10):
        print(f"1/{a} = {1/a}")


def zad15():
    sum = 0
    number = 1
    while number <= 5:
        sum = sum + number
        number = number + 1
    print("Sum of numbers in <1,5> is ", sum)


def zad16():
    a = int(input("1 liczba: "))
    b = int(input("1 liczba: "))

    if a>=b:
        print("Numbers in ascending order: ",b,",",a)
    else:
        print("Numbers in ascending order: ",a,",",b)

def zad17():
    x = 5
    y = 2

    if x*y == 0:
        print("P(", a, ",", b, ") na osi")
    if x*y > 0:
        print("P(", a, ",", b, ") pierwsza ćwiartka")
    if x < 0:
        if y < 0:
            print("P(", a, ",", b, ") trzecia ćwiartka")
        if y > 0:
            print("P(", a, ",", b, ") druga ćwiartka")
    if x > 0:
            print("P(", a, ",", b, ") czwarta ćwiartka")

def zad18():
    amount = int(input("kwota: "))
    zl5 = 0; zl2 = 0; zl1 = 0
    while amount >= 5:
        amount = amount - 5
        zl5 = zl5 + 1
    while amount >= 2:
        amount = amount - 2
        zl2 = zl2 + 1
    while amount >= 1:
        amount = amount - 1
        zl1 = zl1 + 1
    
    print(f"5zl - {zl5}\n2zl - {zl2}\n1zl - {zl1}")  


def zad19():
    wiek = int(input("podaj wiek (liczba całk): "))
    naludzkie = 0   
    while wiek > 2:
        naludzkie = naludzkie + 4
        wiek = wiek - 1
    while wiek != 0:
        naludzkie = naludzkie + 4
        wiek = wiek - 1

    print(f"The dog's age in dog’s years is {naludzkie} years.")

def zad20():
    l = int(input("podaj liczbe: "))
    for a in range(1, 11):
        print(f"{l} x {a} = {l*a}")


def zad21():
    university = "UEK w Krakowie"
    print(university)
    for a in university:
        print(a, "", end = "")

def zad22():
    for a in range(1,31):
        if a % 3 != 0 and a % 5 != 0:
            print(a)
        else:
            if a % 3 == 0 and a % 5 != 0:
                print("THREE")
            else:
                if a % 5 == 0 and a % 3 != 0:
                    print("FIVE")
                else:
                    if a % 5 == 0 and a % 3 == 0:
                        print("BINGO")
       

def zad23():
    liczba = int(input("podaj liczbe wierszy: "))
    for a in range(1, liczba+1):
        for i in range(a):
            print(a, end = "")
        print("")

def zad24():
    liczba = int(input("podaj liczbe wierszy: "))
    
    #kontrola parzystości

    a = int(liczba/2)  
    if liczba % 2 != 0:
        d = a + 2
    else:
        d = a + 1
    
    # d + 1, żeby range zaczynało się od 1

    #1 połowa
    
    for b in range(1, d):
        for c in range(b):
            print("*", end = "")
        print("")

    #2 połowa

    while a != 0:
        for b in range(a):
            print("*", end = "")
        a = a - 1
        print("")

def zad25():
    a = 5; b = 15
    
    for i in range(b):
        print("*", end = "")
    print("")
    
    for x in range(a-2):
        print("*", end = "")
        for y in range(b-2):
            print(" ", end = "")
        print("*")
    
    for i in range(b):
        print("*", end = "")

def zad26():
    pin = "0805"
    flag = 0
    while flag < 3:
        a = input("Enter the PIN code: ")
        if a != pin:
            print("Incorrect...")
            flag = flag + 1
        else:
            print("jeej, koniec programu")
            quit()

    print("Sorry, your payment card has been blocked.")
    quit()

def zad27():
    
    i = 6; j = 1
    while i > -1:    
        while j < 4:    
            print(f' {i+j}',end='')
            j = j + 1
        print()
        j = 1
        i = i - 3

def zad28():
    a = 0; b = 1
    for i in range(25):
        print(a, end = " ")
        print(b, end = " ")
        a = a + b
        b = a + b
    
def zad29():
    summ = 0; counter = 0; a = 1
    while True:
        a = int(input("Enter number: "))
        if a == 0:
            break
        summ = summ + a
        counter = counter + 1

    print(f'RESULT: Quantity={counter}, Sum={summ}, Mean={summ/counter}')

def zad30():
    flag = True
    n = int(input('enter N: '))
    print("prime numbers: 2", end = " ")
    for a in range(3, n+1):
        for i in range(2,a):
            if a % i == 0:
                flag = False
        if flag:
            print(a, end = " ")
        flag = True   

def zad31():
    from random import randrange
    for i in range(20):
        a = randrange(5,10)
        print(a, end = " ")

def zad32():
    for a in range(1,8):
        for b in range(a,a+42, 7):
            if b < 3:
                print(b, end="  ")
            else:
                print(b, end=" ")
        print()
        

#zad10()
#zad11()
#zad12()
#zad13()
#zad15()
#zad16()
#zad17()
#zad18()
#zad19()
#zad20()
#zad21()
#zad22()
#zad23()
#zad24()
#zad25()
#zad26()
#zad27()
#zad28()
#zad29()
#zad30()
#zad31()
#zad32()
