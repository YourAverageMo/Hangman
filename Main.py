import random
import hangman_words
import hangman_art


##### game setup
words = hangman_words.word_list
word = random.choice(words)
lives = 6
print("Welcome to Hangman!")
print(hangman_art.logo)
print(word)
print(f"you have {lives} lives left. Get ready to guess your virtual life away!")
print(hangman_art.stages[lives])

display = []
guesses = []
for position in word:
    display.append("_")
print(display)


##### game logic
while lives > 0 and "_" in display:
    guess = input('guess a letter\n').lower()
    if guess in guesses:
        print(f"What are you dory? You Already guessed '{guess}' dumb dumb.")
        lives -= 1
    else:
        for position in range(len(display)):
            if guess == word[position]:
                display[position] = guess
                guesses += guess
        if guess not in word:
            lives -= 1
            print(f"'{guess}' is not in the word")

    print(hangman_art.stages[lives])
    print(f"you have {lives} lives left")
    print(display)
if lives == 0:
    print("You Lose!")
else:
    print("You Win!")
