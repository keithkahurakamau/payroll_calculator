from payroll import Payroll

def main():
    basic = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))
    
    employee = Payroll(basic, benefits)
    print(f"Gross Salary: {employee.gross_salary}")

if __name__ == "__main__":
    main()