"""Χρήση της match με μοτίβα"""

from enum import IntEnum

class Weekday(IntEnum):
    """Αριθμητική αναπαράσταση των ημερών της εβδομάδας"""
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

def get_weekday_name(day: int) -> str:
    """Επιστρέφει το όνομα της ημέρας της εβδομάδας με βάση τον αριθμό της"""
    match day:
        case Weekday.Saturday | Weekday.Sunday:
            return "Σαββατοκύριακο"
        case _ if Weekday.Monday <= day <= Weekday.Friday:
            return "Εργάσιμη ημέρα"
        case _:
            return "Μη έγκυρη ημέρα"

def main() -> None:

    for day in range(1, 9):
        print(f"Η μέρα {day} είναι : {get_weekday_name(day)}")


if __name__ == "__main__":
    main()