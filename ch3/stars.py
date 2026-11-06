"""Prints 10 asteriks in terminal"""


STARS = 10


def main():
    """Prints 10 asteriks in terminal"""
    i = 1
    while i <= STARS:
        print("*", end="")
        i += 1
    print()         # Εκτύπωση νέας γραμμής μετά τους αστερίσκους


    #Reverse Order


    j = STARS
    while j >= 1:
        print("*", end="")
        j -= 1
    print()


if __name__ == "__main__":
    main()