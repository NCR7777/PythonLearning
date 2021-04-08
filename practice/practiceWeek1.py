# 练习1
TempStr = input()
if TempStr[-1] in ['c', 'C']:
    F = eval(TempStr[0:-1]) * 1.8 + 32
    print("{:.2f}F".format(F))
elif TempStr[-1] in ['f', 'F']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("{:.2f}C".format(C))
else:
    print("输入格式错误")

# 练习2
# template = "零一二三四五六七八九"
# s = input()
# for c in s:
#     print(template[eval(c)], end="")

# 练习3
TempStr = input()
if TempStr[0] in ['c', 'C']:
    # F = 1.8*eval(TempStr[1:]) + 32
    F = eval(TempStr.replace(TempStr[0], "", 1)) * 1.8 + 32
    print("F{:.2f}".format(F))
else:
    # C = (eval(TempStr[1:]) - 32) / 1.8
    C = (eval(TempStr.replace(TempStr[0], "", 1)) - 32) / 1.8
    print("C{:.2f}".format(C))

# 练习4
# CurStr = input()
# if CurStr[:3] == "RMB":
#     print("USD{:.2f}".format(eval(CurStr[3:])/6.78))
# elif CurStr[:3] in ['USD']:
#     print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))
TempStr = input()
ExchangeRate = 6.78
if TempStr[0:3] in ["RMB"]:
    USD = float(TempStr[3:]) / ExchangeRate
    print("USD{:.2f}".format(USD))
elif TempStr[0:3] in ["USD"]:
    RMB = float(TempStr[3:]) * ExchangeRate
    print("RMB{:.2f}".format(RMB))
else:
    print()

# 测验1
TempNum = eval(input())
HelloWorld = "Hello World"
if TempNum == 0:
    print(HelloWorld)
elif TempNum < 0:
    for c in HelloWorld:
        print("{}".format(c))
else:
    for index in range(len(HelloWorld)):
        if index % 2 == 0:
            print("{}".format(HelloWorld[index]), end="")
        else:
            print("{}".format(HelloWorld[index]))

# 测验2
TempResult = input().replace(" ", "")
print("{:.2f}".format(eval(TempResult)))
