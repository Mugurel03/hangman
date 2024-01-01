import random
from wordlists import words_to_guess
from hangman_art import stages


def choose_word():
    generated_word = random.choice(words_to_guess)
    split_word = list(generated_word)
    return split_word


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += " _ "
    return display


def print_hangman(incorrect_guesses, max_attempts):
    remaining_attempts = max_attempts - incorrect_guesses
    if incorrect_guesses < len(stages):
        # Print only the current hangman stage (starting from index 6 and going down)
        current_stage = stages[6 - incorrect_guesses]
        print(current_stage)
        print(f"Remaining attempts: {remaining_attempts}")
    else:
        print("You lost! The correct word was:", ''.join(word_to_guess))


word_to_guess = choose_word()
guessed_letters = []
max_attempts = len(stages)
incorrect_guesses = 0

while True:
    # Display the current state of the word
    current_display = display_word(word_to_guess, guessed_letters)
    print(current_display)

    # Get user input
    user_input = input("Guess a letter: ")

    # Check if the input is a single letter
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a valid single letter.")
        continue

    # Check if the letter has already been guessed
    if user_input in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(user_input)

    # Check if the guessed letter is in the word
    if user_input in word_to_guess:
        print(f"\nThe letter '{user_input}' is correct!")
    else:
        print("\nIncorrect guess.")
        print_hangman(
            incorrect_guesses, max_attempts
        )  # Print the current hangman stage and remaining attempts
        incorrect_guesses += 1

    # Check if the word has been completely guessed
    if set(guessed_letters) >= set(word_to_guess):
        print("Congratulations! You guessed the word:", ''.join(word_to_guess))
        break

    # Check if the player has reached the maximum number of incorrect guesses
    if incorrect_guesses == len(stages) - 1:
        print("\nIncorrect guess.")
        print_hangman(incorrect_guesses, max_attempts
                      )  # Print the final hangman stage and remaining attempts
        print("You lost! The correct word was:", ''.join(word_to_guess))
        break
