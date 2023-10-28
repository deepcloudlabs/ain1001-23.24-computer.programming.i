kate = ("1", "kate austen", 100_000.0, "tr1")
identity, full_name, salary, iban = kate
identity = kate[0]
full_name = kate[1]
salary = kate[2]
iban = kate[3]
print(full_name)
kate = (identity, full_name, 2 * salary, iban)
print(kate)