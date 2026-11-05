"""Sum of integers"""


def main() -> None:
    """Reads two integers from the user, adds them and prints the result"""

    #Data input
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    #Processing - Addition
    result = num1 + num2

    #Prints result
    print(f"Το άθροισμα των {num1} και {num2} είναι {result}")

if __name__ == "__main__":
    main()