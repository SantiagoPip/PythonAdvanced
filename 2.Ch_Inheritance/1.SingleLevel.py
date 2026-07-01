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
        super().__init__(company_name)
        self.employee_name = employee_name
    def employee_info(self):
        response_company = super().info()
        return f"The employee {self.employee_name} works at {response_company}"
    
class Contractor(Company):

    def __init__(self, contractor_name:str,company_name:str):
        self.contractor_name = contractor_name
        super().__init__(company_name)
    def info(self):
        response = super().info()
        return f"The contractor : {self.contractor_name},{response}"

class Manager(Company):
    def __init__(self, manager_name:str,company_name):
        self.manager_name = manager_name
        super().__init__(company_name)
    def info(self):
        response = super().info()
        return f"El manager {self.manager_name} traba en: {response}"
class NewEmployee(Manager):
    def __init__(self,employee_name:str,manager_name:str,company_name:str):
        self.employee_name = employee_name
        super().__init__(manager_name,company_name)
    def info(self):
        response = super().info()
        print(f"The newEmployee name is {self.employee_name} and {response}")

class Client_Company:
    def __init__(self,client_company_name:str):
        self.client_company_name = client_company_name
        
    def info(self):
        print(f"The client company name is {self.client_company_name}")
        return f"The client company name is {self.client_company_name}"

class UltimateEmployee(Company,Client_Company):
    def __init__(self,employee_name:str,company_name,client_company_name:str):
        self.employee_name = employee_name
        self.client_company_name = client_company_name
        self.company_name = company_name
    def info(self):
        response1 = Company.info(self)
        response2 = Client_Company.info(self)
        print(f"The employee {self.employee_name},{response1},{response2}")
        return f"The employee {self.employee_name},{response1},{response2}"


comp_obj = Company("DeppMind")
employee = Employee("Santiago","DeppMind")
#employee.employee_info()

contractor_obj = Contractor("Santiago Moreno","Anthropic")
#contractor_obj.info()

manager_obj = Manager("Diego Cepeda","OpenIA")
#manager_obj.info()

new_employee = NewEmployee("Santiago Moreno ","Camilo Aguilar","Anthropic")
#new_employee.info()

ultimateEmployeeObj = UltimateEmployee("Santiago Moreno","Diego Cepeda","Solution Tech")
ultimateEmployeeObj.info()