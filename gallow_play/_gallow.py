import random


def word_for_guess():
    with open('gallow_play/words_.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines[random.randint(0, len(lines) - 1)]


def gallow(word):
    print(word)
    mistakes = 0
    guessed = ['*' for _ in range(len(word)-1)]
    misses = []
    while (mistakes < len(word)) and ('*' in guessed):
        print('Guess a letter:')
        letter = input()
        if len(letter) > 1 or not letter.isalpha():
            print()
            print('It`s not a letter. Try again!')
        elif letter in guessed:
            print('This letter was guessed.')
        elif letter in misses:
            print('This letter has been already sent.')
        elif letter not in word:
            mistakes += 1
            print('Missed, mistake {} out of {}'.format(mistakes, len(word)))
            misses.append(letter)
        else:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print('Hit!')
        print()
        print("The word:",  ('').join(guessed))
        print()
        print('Misses:', (', '.join(misses)))
        print()
    if mistakes < len(word):
        print('You won!')
    else:
        print('You lost!')