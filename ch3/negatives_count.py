"""Υπολογισμός του αριθμού των αρνητικών αριθμών σε μία λίστα"""


def main() -> None:

    count = 0

    num = int(input("Enter an integer (>0 to exit): "))

    while num < 0:
        count += 1
        num = int(input("Enter an integer (>0 to exit): "))

    print(f"You entered {count} negative numbers")


if __name__ == "__main__":
    main()