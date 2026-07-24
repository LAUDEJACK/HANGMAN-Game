import random
from typing import List
from hangman_art import LOGO, STAGES

WORD_LIST: List[str] = [
             "python", "developer", "software", "galaxy", "hangman", "matrix",
             "love", "jaine", "laude", "obiwan", "morpheus", "luciano", "luciane",
             "laucian", "gustavo", "guinter", "eloise", "family"
]

INITIAL_LIVES: int = 6

def get_user_guess(guessed_letters: List[str]) -> str:
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try another one.")
            continue

        return guess

def play_game() -> None:
    chosen_word = random.choice(WORD_LIST)
    lives = INITIAL_LIVES
    guessed_letters: List[str] = []

    print("\n" + "=" * 30)
    print("NEW HANGMAN GAME")
    print("=" * 30)
    print("_" * len(chosen_word))

    while True:
            guess = get_user_guess(guessed_letters)
            guessed_letters.append(guess)

            display = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
            print(f"\nWord: {display}")

            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed '{guess}', that's not in the word! You lose a life.")

            if lives == 0:
                print(STAGES[lives])
                print(f"\nYOU LOSE! The word was '{chosen_word}'.")
                break

            if "_" not in display:
                print(f"\nYOU WIN! You guessed the word '{chosen_word}'.")
                break

            print(STAGES[lives])

def main() -> None:
    print(LOGO)
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if not play_again.startswith("y"):
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()