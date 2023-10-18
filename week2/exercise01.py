"""
Domain -> sub-domain -> model
 core sub-domain -> hr
"""
from enum import Enum


class FiatCurrency(Enum):
    TL = 1
    EUR = 2
    USD = 3

class Money:
    def __init__(self,value: float,currency: FiatCurrency):
        self.value = value
        self.currency = currency
class FullName:
    def __init__(self,first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class employee:
    def __init__(self,identity: str,full_name: FullName,salary: Money,iban: str):
        self.identity = identity
        self.full_name = full_name
        self.salary = salary
        self.iban = iban

    def increase_salary(self,ratio):
        pass

    def promote(self,department):
        pass