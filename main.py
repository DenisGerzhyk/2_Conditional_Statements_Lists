# 1).

x = int(input())
y = int(input())

z = input('Input symbol *,/,+,-: ')

if z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
elif z == "+":
    print(x + y)
elif z == "-":
    print(x - y)

# 2).

a = [2, 3, 57, 4, 3, 2, 2]

# 1 way
if len(a) == 0:
    print([])
else:
    b = [a[-1]]
    c = b + a
    del (c[-1])
    print(c)

# 2 way
b = [a.pop()]
print(b)
c = b + a
print(c)

# 3).

a = []

if len(a) % 2 == 0:
    middle = len(a) // 2
else:
    middle = len(a) // 2 + 1

first, second = a[:middle], a[middle:]
print([first, second])
