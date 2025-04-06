#add import
from src.question_d.question_d import get_random_number

def main():
    print("Guess a Number!")

    keep_playing = 'y'
    while keep_playing.lower() == 'y':
        random_number = get_random_number()
        correct_guess = False

        while not correct_guess:
            try:
                guess = int(input("Guess a number between 1 and 5: "))
                if 1 <= guess <= 5:
                    if guess == random_number:
                        print("That's correct! Congratulations!")
                        correct_guess = True
                    else:
                        print("Sorry, try again!")
                else:
                    print("Your guess is out of range. Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid integer.")

        keep_playing = input("Play again? (y/n): ")

if __name__ == "__main__":
    main()