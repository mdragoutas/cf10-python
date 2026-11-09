"""Μενού επιλογών με input choice και if-elif-else"""



def print_menu() -> None:

    print("Επιλέξτε μία επιλογή: ")
    print("1. Κατάθεση")
    print("2. Ανάληψη")
    print("3. Υπόλοιπο")
    print("4. Έξοδος")

def main() -> None:
    while True:
        print_menu()
        choice = input("Εισάγετε την επιλογής σας (1-4): ")

        if choice == "1":
            print("Επιλέξατε κατάθεση")

        elif choice == "2":
            print("Επιλέξατε Ανάληψη")

        elif choice == "3":
            print("Επιλέξατε Υπόλοιπο")

        elif choice == "4":
            print("Επιλέξατε Έξοδο")
            break
        else:
            print("Μη έγκυρη επιλογή. Προσπαθήστε ξανά.")


if __name__ == "__main__":
    main()