<<<<<<< HEAD
def user_input_temp() -> int:
    while True:
        try:
            frg_temp = int(input("Enter temperature in F: "))
            return frg_temp
        except ValueError:
            print("Please enter a valid integer.")


def convert_f_to_c(temp_f: float) -> float:
    cels_temp = (temp_f - 32) * 5 / 9
    return round(cels_temp, 1)


def main():
    while True:
        frg_user_temp = user_input_temp()
        cels_temp = convert_f_to_c(frg_user_temp)

        print(f"Temperature in C: {cels_temp}")

        proceed = input("Want to proceed? y/n: ").strip().lower()
        if proceed != 'y':
            break


if __name__ == '__main__':
    main()
=======
from abc import ABC, abstractmethod


class ItEmployee(ABC):
    def __init__(self, emp_id: int ,name: str, surname: str):
        self.name = name
        self.surname = surname
        self.emp_id = emp_id


    @abstractmethod
    def calculate_monthly_salary(self) -> float:
        pass


    @abstractmethod
    def calculate_total_taxes(self) -> float:
        pass


    def print_employee_info(self) -> str:
        print(f"{self.surname} {self.name}")


class HourlyEmployee(ItEmployee):

    def __init__(
            self,
            emp_id: int,
            name: str,
            surname: str,
            hourly_rate: float,
            hours_worked: float = None,
    ):
        super().__init__(emp_id, name, surname)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_monthly_salary(self) -> float:
        if self.hours_worked is not None:
            return self.hourly_rate * self.hours_worked
        return 20.8 * 8 * self.hourly_rate

    def calculate_total_taxes(self) -> float:
        salary = self.calculate_monthly_salary()
        pdfo = salary * 0.18
        vz = salary * 0.015
        return pdfo + vz


class SalariedEmployee(ItEmployee):

    def __init__(
            self,
            emp_id: int,
            name: str,
            surname: str,
            monthly_salary: float,
    ):
        super().__init__(emp_id, name, surname)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self) -> float:
        return self.monthly_salary

    def calculate_total_taxes(self) -> float:
        salary = self.calculate_monthly_salary()
        pdfo = salary * 0.18
        vz = salary * 0.015
        return pdfo + vz


class FopEmployee(ItEmployee):
    def __init__(
            self,
            emp_id: int,
            name: str,
            surname: str,
            hourly_rate: float,
            hours_worked: float = None,
            fop_group: int = 3,
            percent_bonus: float = 0.10,
    ):
        super().__init__(emp_id, name, surname)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.fop_group = fop_group
        self.percent_bonus = percent_bonus

    def calculate_monthly_salary(self) -> float:
        if self.hours_worked is not None:
            base = self.hourly_rate * self.hours_worked
        else:
            base = 20.8 * 8 * self.hourly_rate
        return base * (1 + self.percent_bonus)

    def calculate_total_taxes(self) -> float:
        salary = self.calculate_monthly_salary()
        ep = salary * 0.05
        esv = 1760.0
        return ep + esv


class SelfEmployee(ItEmployee):

    def __init__(
            self,
            emp_id: int,
            name: str,
            surname: str,
            price_per_line: float,
            lines_written: int = None,
    ):
        super().__init__(emp_id, name, surname)
        self.price_per_line = price_per_line
        self.lines_written = lines_written

    def calculate_monthly_salary(self) -> float:
        if self.lines_written is not None:
            return self.price_per_line * self.lines_written
        else:
            return 0.0

    def calculate_total_taxes(self) -> float:
        salary = self.calculate_monthly_salary()
        pdfo = salary * 0.18
        vz = salary * 0.015
        esv = 1760.0
        return pdfo + vz + esv

>>>>>>> 62c6a28 (Lab6 done)
