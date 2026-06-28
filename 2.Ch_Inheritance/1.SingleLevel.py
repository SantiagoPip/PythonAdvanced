#Single level inheritance
class Company:
    title:str = "consultancy"
    def __init__(self,company_name:str):
        self.company_name = company_name
    def info(self):
        print(f"Company name is {self.company_name}")
        return self.company_name
class Employee(Company):
    def __init__(self,employee_name:str,company_name:str):
        self.employee_name = employee_name
        self.company_name = company_name
    def employee_info(self):
        response_company = Company.info(self)
        print(f"The employee {self.employee_name} works at {response_company}")

comp_obj = Company("DeppMind")
employee = Employee("Santiago","DeppMind")
employee.employee_info()