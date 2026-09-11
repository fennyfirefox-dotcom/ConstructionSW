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
