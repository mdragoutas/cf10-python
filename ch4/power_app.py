"""Υπολογισμός της δύναμης ενός αριθμού"""

def power(base: int, exponent: int) -> int:
    """Υπολογίζει την δύναμη της base υψωμένης στο exponent (base^exponent)"""
    result = 1

    for _ in range(exponent):
        result *= base

    return result

def main():

    for base, exponent in ((2, 3) , (3, 4), (5, 2)):
        result = power(base, exponent)

        print(f"{base}^{exponent} = {result}")


if __name__ == "__main__":
    main()