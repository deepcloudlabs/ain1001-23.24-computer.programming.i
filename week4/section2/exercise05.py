employees = {
    "1" : {"fullname": "kate austen", "salary": 100_000, "department": ["IT"]},
    "42" : {"fullname": "jack austen", "salary": 125_000, "department": ["FINANCE","SALES"]}
}
print("42" in employees)
print(employees["42"]["salary"])
employees["549"] = {"fullname": "james sawyer", "salary": 50_000, "department": ["HR"]}
for identity in employees:
    employees[identity]["salary"] *= 2
for identity in employees:
    print(employees[identity]["salary"])
print(len(employees))
print(employees.keys())
print(employees.values())
print(len(employees))
for employee in employees.values():
    print(employee)
