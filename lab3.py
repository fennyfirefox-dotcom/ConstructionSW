import doctest
import sys


def reverse_words(text: str) -> str:
    """
    >>> reverse_words("abcd")
    'dcba'
    >>> reverse_words("abcd efgh")
    'dcba hgfe'
    >>> reverse_words("")
    ''
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'
    >>> reverse_words(123)
    Traceback (most recent call last):
        ...
    TypeError: Переданий аргумент повинен бути строкою (str).
    """
    if not isinstance(text, str):
        raise TypeError("Переданий аргумент повинен бути строкою (str).")

    if not text.isascii():
        raise ValueError("Текст повинен містити тільки ASCII символи.")

    def reverse_single_word(word: str) -> str:
        letters = [char for char in word if char.isalpha()]
        result = []

        for char in word:
            if char.isalpha():
                result.append(letters.pop())
            else:
                result.append(char)

        return "".join(result)

    words = text.split(" ")
    reversed_words = [reverse_single_word(w) for w in words]

    return " ".join(reversed_words)


def run_interactive_mode():
    print("Введіть 'exit' або 'quit' для виходу.\n")

    while True:
        try:
            user_input = input("Введіть текст: ")

            if user_input.strip().lower() in ("exit", "quit"):
                print("Завершення роботи.")
                break

            result = reverse_words(user_input)
            print(f"Результат: {result}\n")

        except ValueError as ve:
            print(f"Помилка введення: {ve}\n")
        except KeyboardInterrupt:
            print("\nПрограму примусово завершено.")
            break
        except Exception as e:
            print(f"Виникла непередбачена помилка: {e}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Запуск doctest...")
        failures, tests = doctest.testmod()
        print(f"Тестування завершено: {tests - failures}/{tests} тестів пройдено успішно.")
    else:
        failures, _ = doctest.testmod()
        if failures == 0:
            run_interactive_mode()
        else:
            print("Виявлено помилки у функціоналі! Запуск зупинено.")