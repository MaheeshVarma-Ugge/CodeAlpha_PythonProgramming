import random
words = ['python', 'algorithm', 'variable', 'function', 'keyboard']
secret = random.choice(words)
guessed = set()
wrong = 0
MAX_WRONG = 6

print("Welcome to Hangman!")
print(f"The word has {len(secret)} letters.\n")

while wrong < MAX_WRONG:
    display = ' '.join(ch if ch in guessed else '_' for ch in secret)
    print(f"Word: {display}")
    print(f"Wrong guesses left: {MAX_WRONG - wrong}")
    print(f"Missed: {' '.join(sorted(g for g in guessed if g not in secret))}")

    if all(ch in guessed for ch in secret):
        print(f"\n🎉 You won! The word was: {secret.upper()}")
        break

    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue
    if guess in guessed:
        print("Already guessed that!\n")
        continue

    guessed.add(guess)
    if guess not in secret:
        wrong += 1
        print(f"❌ Wrong! ({wrong}/{MAX_WRONG})\n")
    else:
        print(f"✅ Good guess!\n")
else:
    print(f"\n💀 Game over! The word was: {secret.upper()}")