"""Ανάληψη απο ATM"""

EXIT_VALUE = 0
BANKNOTE = 20
INITIAL_BALANCE = 1000

def main() -> None:
    """Εκτελεί αναλήψεις ελέγχοντας πρώτα τα error states"""
    balance = INITIAL_BALANCE

    while True:
        print(f"Your current balance is: {balance}")
        amount = int(input("Please select an amount you would like to withdraw (0 to Exit): "))

        if amount == EXIT_VALUE:
            print("Exiting...")
            break

        if amount > balance:
            print("Error: Your balance is insufficient")
            continue

        if amount % BANKNOTE != 0:
            print(f"Error: The amount must be multiple of {BANKNOTE}")
            continue


        balance -= amount
        print(f"The withdrawal of {amount} euros is complete. Your new balance is {balance}")


if __name__ == "__main__":
    main()