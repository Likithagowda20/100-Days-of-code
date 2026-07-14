class Employee:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company
    
    def details(self):
        print(f"{self.name} works at {self.company} and earns {self.salary}")
    
    def appraisal(self):
        print (f"{self.name} has received an appraisal of {self.salary * 0.1} this year.")

emp1 = Employee("Raj", 50000, "Google")
emp2 = Employee("Priya", 60000, "Amazon")
emp3 = Employee("Ram",90000,"Deloitte")

emp1.details()
emp2.details()
emp3.details()
emp3.appraisal()