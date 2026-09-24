def get_positive_number(prompt: str, is_float: bool = False):
    while True:
        try:
            val = float(input(prompt)) if is_float else int(input(prompt))
            if val <= 0:
                print("Значення має бути більше 0!")
                continue
            return val
        except ValueError:
            print("Будь ласка, вводьте тільки числа!")


def user_input() -> tuple[int, float, int]:
    amount_dep = get_positive_number("Enter the amount deposited: ")
    per_year = get_positive_number("Enter the annual interest rate (0.12 for 12%): ", is_float=True)
    exp_date = 24  # months
    return amount_dep, per_year, exp_date


def calc_per_month(amount: int, per_year: float) -> float:
    return (amount * per_year) / 12


def calc_full_amount(amount: int, dep_month: float, exp_date: int) -> float:
    return amount + (dep_month * exp_date)


def main():
    amount, per_year, exp_date = user_input()

    monthly_profit = calc_per_month(amount, per_year)
    total_amount = calc_full_amount(amount, monthly_profit, exp_date)

    total = amount
    for i in range(1, exp_date + 1):
        total += monthly_profit
        print(f"Month: {i:2d}, Profit: {monthly_profit:.2f}, Total amount: {total:.2f}")

    print(f"Total amount after {exp_date} months: {total_amount:.3f}")


if __name__ == '__main__':
    main()