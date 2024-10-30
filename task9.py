# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
def two(N):
    if N==1:
        return True
    elif N%2==0:
        return two(N//2)
    else:
        return False
N = int(input())
if two(N):
    print("YES")
else:
    print("NO")
