kate = ("11111111110", "kate austen",
        100_000., "tr1", 1996, "IT", "FULL TIME")
print(kate[2])
# kate[2] = 1.5 * kate[2]
# del kate[4]
identity, full_name, salary, iban, birth_year, department, job_style = kate
print(department)
print(full_name)
print(kate)
kate = (identity, full_name, 1.5 * salary, iban, birth_year, department, job_style)
print(kate)
numbers = (4, 8, 14, 15, 42, 108, 8, 4, 8)
print(len(numbers))
# print(numbers[-10])
print(42 in numbers)
print(3615 in numbers)
for number in numbers:
    print(number)