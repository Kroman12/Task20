def comparison(number):
    if number > 100:
        print ("Sorry, you're dead.")
    elif number >= 65:
        print ("Enjoy your retirement!")
    elif number >= 40:
        print ("You're over the hill.")
    elif number == 21:
        print ("Congrats on your 21st!")
    elif number < 13:
        print ("You qualify for the kiddie discount.")
    else:
        print ("Age is but a number.")


while True:
    try:
        age = int(input("\nPlease enter your age: "))
        comparison(age)
    except ValueError:
        print ("Invalid number.")

