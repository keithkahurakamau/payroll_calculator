# nss_net.py

class Payroll:
    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.gross_salary = self.basic_salary + self.benefits

    def calculate_paye(self):
        #calculate PAYE based KRA tax bands
        if self.gross_salary <= 24000:
            return self.gross_salary * 0.1
        elif self.gross_salary <= 32333:
            return self.gross_salary * 0.25
        else:
            return self.gross_salary * 0.3

    def calculate_nhif(self):
        #NHIF deduction
        if self.gross_salary <= 5999:
            return 150
        elif self.gross_salary <= 7999:
            return 300
        else:
            return 500

    # NSSF method
    def calculate_nssf(self):
        # 6% of gross salary
        nssf_amount = self.gross_salary * 0.06
        return nssf_amount

    # Net salary method
    def calculate_net_salary(self):
        #calculate net salary after deducting PAYE, NHIF, and NSSF
        return self.gross_salary - (
            self.calculate_paye() +
            self.calculate_nhif() +
            self.calculate_nssf()
        )
