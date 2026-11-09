

def main() -> None:

    count = 0

    # while (num:= int(input("Εισάγετε έναν ακέραιο αριθμό (>=0 για έξοδο): "))) < 0:
    #     count += 1

    while True:
        num = int(input("Enter an integer (>=0 to exit): "))

        if num >= 0:
            break

        count += 1

        print(f"Ο αριθμός των αρνητικών αριθμών που εισήχθησαν έιναι: {count}")


if __name__ == "__main__":
    main()