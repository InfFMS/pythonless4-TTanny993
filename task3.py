# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
def a(num):
    wtf=[1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    rim=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    r=""
    i = 0
    while num>0:
        for j in range(num//wtf[i]):
            r+=rim[i]
            num-=wtf[i]
        i+=1
    return r

N=int(input())
print(a(N))

