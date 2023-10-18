x = 42
y = 108
t = x
x = y
y = t
print(x, y)
x, y = y, x
print(x, y)
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)
