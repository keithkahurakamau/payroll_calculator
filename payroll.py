class Payroll:
    #constructor method to initialize basic salary and benefits
    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        #calculate gross salary and store
        self.gross_salary = self.calculate_gross_salary()

    def calculate_gross_salary(self):
        #add basic salary and benefits to get gross salary
        return self.basic_salary + self.benefits
    
    def calculate_paye(self):
        monthly_salary = self.gross_salary
        annual_salary = monthly_salary * 12
        
        #KRA tax bands
        if annual_salary <= 288000: #first 288000 at 10%
            tax = 0.1 * annual_salary
        elif annual_salary <= 388000: #next 100000 at 25%
            tax = 288000 * 0.10 + (annual_salary - 288000) * 0.25
        elif annual_salary <= 6000000: #next up to 6,000 000 at 30%
            tax = 288000 * 0.10 + 100000 * 0.25 + (annual_salary - 388000) * 0.30
        elif annual_salary <= 9600000: #next up to 9,600,000 at 32.5%
            tax = 288000 * 0.10 + 100000 * 0.25 + 5612000 * 0.30 + (annual_salary - 6000000) * 0.325
        else: #over 9,600,000 at 35%
            tax = 288000 * 0.10 + 100000 * 0.25 + 5612000 * 0.30 + 3600000 * 0.325 + (annual_salary - 9600000) * 0.35
            
        # subtract annual personal relief of 28800 before calculating monthly PAYE
        tax = max(0, tax - 28800)
        
        #convert back to monthly paye
        return tax / 12
    
    def calculate_nhif(self):
        #using SHIF rates
        return self.gross_salary * 0.0275
       

if __name__ == "__main__":
    #user input
    basic = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))    
    #create Payroll object
    employee = Payroll(basic, benefits)
    #display results
    print(f"Gross Salary: {employee.gross_salary}")
    print(f"PAYE: {employee.calculate_paye()}")
    print(f"NHIF: {employee.calculate_nhif()}")
    
    