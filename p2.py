from datetime import datetime, timedelta, date
import time, random
from itertools import product

# Exc 7
def guessing_game():
    number = random.randint(1, 20)
    print("I picked a number between 1 and 20.")
    print("You have 5 seconds to guess it!")

    start = datetime.now()
    guess = input("Your guess: ")
    elapsed = datetime.now() - start

    if elapsed > timedelta(seconds=5):
        print("Time is up, you lose")
        print(f"The number was {number}.")
    elif guess.isdigit() and int(guess) == number:
        print("Correct, you win!")
    else:
        print(f"Wrong! The number was {number}.")

# guessing_game()


# Exc 8
def race():
    start = datetime.now()

    player1 = start + timedelta(seconds=random.randint(5, 20))
    player2 = start + timedelta(seconds=random.randint(5, 20))

    time1 = (player1 - start).seconds
    time2 = (player2 - start).seconds

    print(f"Player 1 finished in {time1} seconds")
    print(f"Player 2 finished in {time2} seconds")

    if player1 < player2:
        print("Player 1 wins!")
    elif player2 < player1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# race()


# Exc 9
def days_until_birthday(birthday):
    today = date.today()
    next_birthday = date(today.year, birthday.month, birthday.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, birthday.month, birthday.day)

    days_left = (next_birthday - today).days
    return days_left

# birth_year = int(input("Enter your birth year: "))
# birth_month = int(input("Enter your birth month (1-12): "))
# birth_day = int(input("Enter your birth day (1-31): "))
# birthday = date(birth_year, birth_month, birth_day)
# print(days_until_birthday(birthday))


# Exc 10
def crack_safe():
    # computer generates a random 4-digit password, each digit 1-6
    password = tuple(random.randint(1, 6) for _ in range(4))

    # try every possible combination until we match
    for attempt in product(range(1, 7), repeat=4):
        print(attempt)
        if attempt == password:
            print("Password is correct, the vault is open")
            break

# crack_safe()