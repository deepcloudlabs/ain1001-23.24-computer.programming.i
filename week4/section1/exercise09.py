employees = {
    "1": ("kate austen", 100_000.0, "tr1", 1990, "FINANCE", "FULL TIME"),
    "2": ("jack shephard", 200_000.0, "tr2", 1980, "IT", "PART TIME")
}

employees = {
    "IT": [("kate austen", 100_000.0, "tr1", 1990, "IT", "FULL TIME"),
           ("jack shephard", 200_000.0, "tr2", 1980, "IT", "PART TIME")]
}

employees = {
    "IT": [
           {"full_name": "kate austen",
            "salary": 100_000.0,
            "iban": "tr1",
            "birth_year": 1990,
            "department": "IT",
            "job_style": "FULL TIME"
            },
           {"full_name": "jack shephard",
            "salary": 200_000.0,
            "iban": "tr2", "birth_year": 1980,
            "department": "IT",
            "job_style": "PART TIME"}
           ]
}
employees = {
    "FULL TIME": [
           {"full_name": "kate austen",
            "salary": 100_000.0,
            "iban": "tr1",
            "birth_year": 1990,
            "department": "IT",
            "job_style": "FULL TIME"
            }],
    "PART TIME": [
           {"full_name": "jack shephard",
            "salary": 200_000.0,
            "iban": "tr2", "birth_year": 1980,
            "department": "IT",
            "job_style": "PART TIME"}
           ]
}

employees["IT"][0]
employees["IT"][-1]
len(employees["IT"])