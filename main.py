from payroll import Payroll # import the Payroll class from the payroll module

def main():
    #take user input for basic salary and benefits
    basic = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))
    #create Payroll object using user input
    employee = Payroll(basic, benefits)
    #display gross salary
    print(f"Gross Salary: {employee.gross_salary}")

# ensure main runs only when this file is executed directly
if __name__ == "__main__":
    main()