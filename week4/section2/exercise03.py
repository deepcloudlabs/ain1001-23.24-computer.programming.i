numbers = [4, 8, 14, 15, 42, 108, 8, 4, 8, float("nan")]
print(numbers)
numbers.append(549)
print(numbers)
numbers.insert(3, 3615)
print(numbers)
print(numbers.pop(3))
print(numbers)
while 8 in numbers:
    numbers.remove(8)
print(numbers)
print(42 in numbers)
print(float("nan") in numbers)
for number in numbers:
    print(number)