import pandas as pd
from pydantic import BaseModel


class CalculateSalary:
    min_salary = float('inf')
    max_salary = 0
    min_index = []
    max_index = []

    @classmethod
    def min_max_salary(cls, information):
        for index, info in enumerate(information):
            if info.salary < cls.min_salary:
                cls.min_salary = info.salary
                cls.min_index = [index]
            elif info.salary == cls.min_salary:
                cls.min_index.append(index)

            if info.salary > cls.max_salary:
                cls.max_salary = info.salary
                cls.max_index = [index]
            elif info.salary == cls.max_salary:
                cls.max_index.append(index)

    @classmethod
    def display_result(cls, information):
        for index in cls.min_index:
            print(f"Name: {information[index].name}, Salary: {information[index].salary}")
        for index in cls.max_index:
            print(f"Name: {information[index].name}, Salary: {information[index].salary}")


class Info(BaseModel):
    name: str
    salary: int


information = []
file = pd.read_csv("files/salarysheet.csv")
print("File content:\n", file)
for index, row in file.iterrows():
    info = Info(name=row['name'], salary=row['salary'])
    information.append(info)

CalculateSalary.min_max_salary(information)
CalculateSalary.display_result(information)

