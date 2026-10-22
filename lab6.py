import argparse
import random
from faker import Faker

from l import (
    ItEmployee,
    HourlyEmployee,
    SalariedEmployee,
    FopEmployee,
    SelfEmployee,
)

fake = Faker("uk_UA")


def get_employee_type_name(employee: ItEmployee) -> str:
    if isinstance(employee, HourlyEmployee):
        return "Hourly"
    elif isinstance(employee, SalariedEmployee):
        return "Salaried"
    elif isinstance(employee, FopEmployee):
        return "FOP"
    elif isinstance(employee, SelfEmployee):
        return "Per-line"
    return "Unknown"


def generate_employees(amount: int = 20) -> list[ItEmployee]:
    employees = []
    for i in range(1, amount + 1):
        emp_type = random.choice(["hourly", "salaried", "fop", "self_employed"])
        first_name = fake.first_name()
        last_name = fake.last_name()

        if emp_type == "hourly":
            emp = HourlyEmployee(
                emp_id=i,
                name=first_name,
                surname=last_name,
                hourly_rate=random.randint(15, 50),
            )
        elif emp_type == "salaried":
            emp = SalariedEmployee(
                emp_id=i,
                name=first_name,
                surname=last_name,
                monthly_salary=random.randint(2000, 6000),
            )
        elif emp_type == "fop":
            emp = FopEmployee(
                emp_id=i,
                name=first_name,
                surname=last_name,
                hourly_rate=random.randint(20, 60),
                fop_group=random.choice([2, 3]),
            )
        else:
            emp = SelfEmployee(
                emp_id=i,
                name=first_name,
                surname=last_name,
                price_per_line=random.uniform(0.5, 2.5),
                lines_written=random.randint(1000, 4000),
            )
        employees.append(emp)
    return employees


def get_sort_key(employee: ItEmployee):
    return (-employee.calculate_monthly_salary(), employee.surname)


def sort_employees(employees: list[ItEmployee]) -> list[ItEmployee]:
    return sorted(employees, key=get_sort_key)


def print_employees(employees: list[ItEmployee]):
    print("=========================================================================================")
    print("ID | Name and Surname          | Salary   | Tax      | Type")
    print("=========================================================================================")

    total_tax = 0.0
    for e in employees:
        salary = e.calculate_monthly_salary()
        tax = e.calculate_total_taxes()
        emp_type = get_employee_type_name(e)
        total_tax += tax

        full_name = f"{e.surname} {e.name}"
        print(f"{e.emp_id:<2} | {full_name:<25} | {salary:<8.2f} | {tax:<8.2f} | {emp_type}")

    print("=========================================================================================")
    print(f"Total tax: {total_tax:.2f}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-income", type=float)
    parser.add_argument("--max-tax", type=float)
    parser.add_argument("--fop-group", type=int)

    args = parser.parse_args()

    employees = generate_employees(20)
    sorted_emp = sort_employees(employees)

    filtered = []
    for e in sorted_emp:
        if args.fop_group is not None:
            if not (isinstance(e, FopEmployee) and e.fop_group == args.fop_group):
                continue

        if args.min_income is not None:
            if e.calculate_monthly_salary() < args.min_income:
                continue

        if args.max_tax is not None:
            if e.calculate_total_taxes() > args.max_tax:
                continue

        filtered.append(e)

    print_employees(filtered)


if __name__ == "__main__":
    main()