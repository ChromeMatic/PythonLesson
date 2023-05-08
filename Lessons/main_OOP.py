class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def __str__(self):
        return f"{self.first} {self.last} {self.email} ${self.pay}"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self, raise_amount):
        self.pay = int(self.pay * (1 + raise_amount))


emp1 = Employee("Alex", "Jones", 50000)
emp2 = Employee("Jack", "Mason", 50000)
emp2.apply_raise(0.05)

print(emp1.fullname())
print(emp1.pay)

print(emp2.fullname())
print(emp2.pay)
