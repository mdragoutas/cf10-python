"""Υπολογισμός της άθροισης των n πρώτων φυσικών αριθμών"""

def sum_of_first_n(n: int) -> int:
    """Υπολογίζει το άρθοισμα των n πρώτων φυσικών αριθμών"""

    total_sum = 0
    i = 1
    while i <= n:
        total_sum += i
        i += 1


    return total_sum

def main():

    n = 10
    result = sum_of_first_n(n)
    print(f"Το άρθοισμα των {n} πρώτων φυσικών αριθμών είναι: {result}")