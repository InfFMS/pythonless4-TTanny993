# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
def rt(n):
    i=0
    while n:
        i+= n % 10
        n //= 10
        if n:
            i *= 10
    print(i)
n = int(input())
rt(n)