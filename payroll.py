class Payroll:
    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.gross_salary = self.calculate_gross_salary()
    
    def calculate_gross_salary(self):
        return self.basic_salary + self.benefits
