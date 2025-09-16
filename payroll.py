class Payroll:
    #take employee basic salary and benefits as input
    def __init__(self, basic_salary, benefits):
        #store employee's basic monthly salary 
        self.basic_salary = basic_salary
        #store the total value of benefits
        self.benefits = benefits
        #calculate gross salary
        self.gross_salary = self.calculate_gross_salary()
    
    def calculate_gross_salary(self):
        #add basic salary and benefits to get gross salary
        return self.basic_salary + self.benefits 
