"""Υπολογίζει το παραγοντικό !n ενός ακεραίου n που δίνεται από τον χρήστη"""

def facto_of_n(n: int) -> int:
    facto = 1

    i = n
    while i >= 1:
        facto *= i
        i -= 1

    return facto

def main() -> None:
    n = int(input("Παρακαλώ είσαγετε έναν ακέραιο αριθμό: "))
    result = facto_of_n(n)

    print(f"Το παραγοντικό του αριθμού {n} ισούται με {result}.")


if __name__ == "__main__":
    main()