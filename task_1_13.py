import math

x = input("x=")
x = float(x)
a = input("a=")
a = float(a)
a = math.radians(a)
print(a)

while a < 0:
    a = 2 * (math.pi)
while a >= 2 * (math.pi):
    a -= 2 * (math.pi)
print(a)

if (abs(x) <= 2) | (x < 0):
    print("Ошибка значения числа х, введите x заново")
if (a == math.pi) | (a == 0):
    print("Ошибка значения числа a, на 0 делить нельзя")
else:
    ans = (math.log1p(x ** 3 - 8) + 1 / math.sin(a))
    print(ans)
