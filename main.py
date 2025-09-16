from payroll import Payroll

def main():
    basic = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))
    
    employee= Payroll(basic, benefits)
    paye = employee.calculate_paye()
    nhif = employee.calculate_nhif()

    print(f"Gross Salary: {employee.gross_salary}")
    print(f"PAYE: {paye}")
    print(f"NHIF: {nhif}")

if __name__ == "__main__":
    main()