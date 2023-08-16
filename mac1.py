def FPin(i,n):
    return (1+i)**n

def PFin(i,n):
    return (1+i)**-n

def FAin(i,n):
    return ((1+i)**n-1)/i

def AFin(i,n):
    return i/((1+i)**n-1)

def PAin(i,n):
    return (1-(1+i)**-n)/i

def APin(i,n):
    return i/(1-(1+i)**-n)

def FAin1i(i,n):
    return (1+i)**(n+1)-1

def PAin1i(i,n):
    return (1-(1+i)**-(n-1))/i


while True:
    print("现值和终值系数计算")
    print("1,复利终值系数")
    print("2,复利现值系数")
    print("3,普通年金终值系数")
    print("4,年偿债基金系数")
    print("5,普通年金现值系数")
    print("6,年资本回收系数")
    print("7,预付年金终值系数")
    print("8,预付年金现值系数")
    print("9,递延年金终值")
    cmd = input(">")
    if cmd=="exit":
        exit()
    elif cmd == "1":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(FPin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "2":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(PFin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "3":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(FAin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "4":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(AFin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "5":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(PAin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "6":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(APin(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "7":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(FAin1i(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "8":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(PAin1i(i,n))
                print("*"*20)
            except:
                  pass
    elif cmd == "9":
            try:
                i = float(input("请输入i的值："))
                n = float(input("请输入n的值："))
                print("*"*20)
                print(FAin(i,n))
                print("*"*20)
            except:
                  pass
    else:
        print("*"*20)
        print("给定了个错误的值！")
        print("*"*20)
        pass