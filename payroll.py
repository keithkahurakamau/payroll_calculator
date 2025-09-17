class Payroll:
    def __init__(self, basic_salary, benefits):
        """
        Initialize the Payroll object with basic salary and benefits.
        Calculate and store the gross salary.
        """
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.gross_salary = self.calculate_gross_salary()

    def calculate_gross_salary(self):
        """
        Calculate the gross salary by adding basic salary and benefits.
        Returns:
            float: The gross salary.
        """
        return self.basic_salary + self.benefits

    def calculate_paye(self):
        """
        Calculate the PAYE (tax) based on the gross salary using the tax bands from Aren.co.ke (2023).
        Applies personal relief of 2400 Ksh monthly.
        Returns:
            float: The monthly PAYE tax after relief.
        """
        monthly_salary = self.gross_salary
        # PAYE tax bands
        if monthly_salary <= 24000:
            tax = 0.10 * monthly_salary
        elif monthly_salary <= 32333:
            tax = 24000 * 0.10 + (monthly_salary - 24000) * 0.25
        elif monthly_salary <= 500000:
            tax = 24000 * 0.10 + (32333 - 24000) * 0.25 + (monthly_salary - 32333) * 0.30
        elif monthly_salary <= 800000:
            tax = 24000 * 0.10 + (32333 - 24000) * 0.25 + (500000 - 32333) * 0.30 + (monthly_salary - 500000) * 0.325
        else:
            tax = 24000 * 0.10 + (32333 - 24000) * 0.25 + (500000 - 32333) * 0.30 + (800000 - 500000) * 0.325 + (monthly_salary - 800000) * 0.35

        # Apply personal relief
        tax = max(0, tax - 2400)
        return tax

    def calculate_nhif(self):
        """
        Calculate the NHIF deduction based on gross salary using NHIF brackets.
        Returns:
            int: The NHIF deduction amount.
        """
        if self.gross_salary <= 5999:
            return 150
        elif self.gross_salary <= 7999:
            return 300
        elif self.gross_salary <= 11999:
            return 400
        elif self.gross_salary <= 14999:
            return 500
        elif self.gross_salary <= 19999:
            return 600
        elif self.gross_salary <= 24999:
            return 750
        elif self.gross_salary <= 29999:
            return 850
        elif self.gross_salary <= 34999:
            return 900
        elif self.gross_salary <= 39999:
            return 950
        elif self.gross_salary <= 44999:
            return 1000
        elif self.gross_salary <= 49999:
            return 1100
        elif self.gross_salary <= 59999:
            return 1200
        elif self.gross_salary <= 69999:
            return 1300
        elif self.gross_salary <= 79999:
            return 1400
        elif self.gross_salary <= 89999:
            return 1500
        elif self.gross_salary <= 99999:
            return 1600
        else:
            return 1700

    def calculate_nssf(self):
        """
        Calculate the NSSF deduction as 6% of the gross salary.
        Returns:
            float: The NSSF deduction amount.
        """
        return self.gross_salary * 0.06

    def calculate_net_salary(self):
        """
        Calculate the net salary by subtracting PAYE, NHIF, and NSSF deductions from gross salary.
        Returns:
            float: The net salary.
        """
        return self.gross_salary - (
            self.calculate_paye() +
            self.calculate_nhif() +
            self.calculate_nssf()
        )
