"""Convert hours to minutes and seconds"""

MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    """Διαβάζει τον αριθμό ωρών από τον χρήστη και εκτπώνει τον αντίστοιχο αριθμό λεπτών και δευτερολέπτων"""

    #Data input
    hours = int(input("Εισάγετε τον αριθμό των ωρών: "))

    #Processing - Conversion of hours to minutes and seconds
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    #Result - Printing the outcome
    print(f"{hours} ώρες ισοδυναμούν με {minutes} λεπτά ή {seconds} δευτερόλεπτα")

if __name__ == "__main__":
    main()