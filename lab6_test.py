import unittest

from l import HourlyEmployee, SalariedEmployee, FopEmployee, SelfEmployee
from lab6 import (
    generate_employees,
    sort_employees,
    get_sort_key,
    get_employee_type_name,
)


class TestEmployeeSystem(unittest.TestCase):

    def setUp(self):
        self.emp_hourly = HourlyEmployee(
            emp_id=1, name="John", surname="Doe", hourly_rate=20.0
        )
        self.emp_salaried = SalariedEmployee(
            emp_id=2, name="Alice", surname="Smith", monthly_salary=3000.0
        )
        self.emp_fop2 = FopEmployee(
            emp_id=3, name="Bob", surname="Johnson", hourly_rate=30.0, fop_group=2
        )
        self.emp_fop3 = FopEmployee(
            emp_id=4, name="Emma", surname="Brown", hourly_rate=40.0, fop_group=3
        )
        self.emp_self = SelfEmployee(
            emp_id=5,
            name="Charlie",
            surname="Davis",
            price_per_line=1.5,
            lines_written=2000,
        )

    def test_generate_employees_amount(self):
        employees = generate_employees(15)
        self.assertEqual(len(employees), 15)

    def test_get_employee_type_name(self):
        self.assertEqual(get_employee_type_name(self.emp_hourly), "Hourly")
        self.assertEqual(get_employee_type_name(self.emp_salaried), "Salaried")
        self.assertEqual(get_employee_type_name(self.emp_fop2), "FOP")
        self.assertEqual(get_employee_type_name(self.emp_self), "Per-line")

    def test_get_sort_key(self):
        key = get_sort_key(self.emp_salaried)
        self.assertEqual(key, (-3000.0, "Smith"))

    def test_sort_employees(self):
        employees = [self.emp_hourly, self.emp_salaried, self.emp_self]
        sorted_list = sort_employees(employees)

        for i in range(len(sorted_list) - 1):
            sal1 = sorted_list[i].calculate_monthly_salary()
            sal2 = sorted_list[i + 1].calculate_monthly_salary()
            self.assertGreaterEqual(sal1, sal2)

    def test_filter_fop_group(self):
        employees = [self.emp_hourly, self.emp_fop2, self.emp_fop3, self.emp_salaried]

        fop_group_2 = [
            e for e in employees
            if isinstance(e, FopEmployee) and e.fop_group == 2
        ]

        self.assertEqual(len(fop_group_2), 1)
        self.assertEqual(fop_group_2[0].surname, "Johnson")

    def test_filter_by_income(self):
        low_hourly = HourlyEmployee(
            emp_id=1, name="John", surname="Doe", hourly_rate=10.0
        )
        employees = [self.emp_salaried, low_hourly]
        min_income = 2500.0

        filtered = [
            e for e in employees
            if e.calculate_monthly_salary() >= min_income
        ]

        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.emp_salaried)

if __name__ == "__main__":
    unittest.main()