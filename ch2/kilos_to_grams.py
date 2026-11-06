"""Converts kilograms to grams"""

GRAMS_IN_KILOS = 1000

def main():
    kilos = int(input("Enter the kilograms: "))
    grams = kilos * GRAMS_IN_KILOS
    print(f"{kilos} kilograms are equal to {grams} grams.")

if __name__ == "__main__":
    main()