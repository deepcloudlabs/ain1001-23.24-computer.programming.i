employees: list[str] = ["kate austen", "jack shephard", "james sawyer", "ben linus", "sun kwon", "jin kwon"]
print(employees[0])
print(employees[-1])
employees.append("jack bauer")
print(employees[-1])
print(employees[3])
del employees[3]
print(employees[3])
print(employees[0])
employees[0] = "kate shephard"
print(employees[0])


