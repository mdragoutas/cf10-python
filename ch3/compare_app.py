"""Αλυσιδωτές συγκρίσεις"""


MIN_GRADE = 50
MAX_GRADE = 100


def is_passing(grade: int) -> bool:
    """Επιστρέφει True αν η βαθμολογία βρίσκεται μεταξύ 50 και 100, αλλιώς False """
    return MIN_GRADE <= grade <= MAX_GRADE


def main():
    for grade in (80, 90, 40, 30):
        is_grade_passing = is_passing(grade)
        print(f"Η βαρθμολογία {grade} είναι επιτυχής: {is_grade_passing}")

    print()


if __name__ == "__main__":
    main()