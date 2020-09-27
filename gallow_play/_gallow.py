import random


def word_for_guess():
    with open('gallow_play/words_.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines[random.randint(0, len(lines) - 1)]

class Gallow:

    def __init__(self, word):
        self.word = word
        self.mistakes = 0
        self.guessed = ['*' for _ in range(len(self.word))]
        self.misses = []

    def decision(self, letter):
        if len(letter) > 1 or not letter.isalpha():
            print()
            print('It`s not a letter. Try again!')
        elif letter in self.guessed:
            print('This letter was guessed.')
        elif letter in self.misses:
            print('This letter has been already sent.')
        elif letter not in self.word:
            self.mistakes += 1
            print('Missed, mistake {} out of {}'.format(self.mistakes, len(self.word)))
            self.misses.append(letter)
        else:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed[i] = letter
            print('Hit!')
        print()
        print("The word:",  ('').join(self.guessed))
        print()
        print('Misses:', (', '.join(self.misses)))
        print()

    def gallow(self):
        print(self.word)
        while (self.mistakes < len(self.word)) and ('*' in self.guessed):
            letter = input('Guess a letter: \n')
            self.decision(letter)
        if self.mistakes < len(self.word):
            print('You won!')
        else:
            print('You lost!')
