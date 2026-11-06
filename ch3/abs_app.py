"""Απόλυτη τιμή ενός ακεραίου με conditional expression"""


def abs_n(n : int) -> int:
    return n if n > 0 else -n


def main() -> None:
    n = int(input("Enter a number: "))

    print(f"The absolute value of {n} is {abs_n(n)}")


if __name__ == "__main__":
    main()