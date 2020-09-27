# The project "gallow"

[![Build Status][travis-badge]][travis-url]
[![Coverage][coverage-image]][coverage-url]

It's a pleasnt play for you and your friends.

## Downloading and starting

Clone this repo to your local machine

```
git clone https://github.com/Verbarius/Software-architecture
```

Go to the repo and write  

```
python3 ./main.py
```

## The process of play

You aim is to guess the word, which programm proposes for you. You'll see the following text

```
Guess a letter:
```
You need to enter just one letter, which you think is in the word. Don't try to enter numbers or combinations of letters, programm will not accept it.

You have as many attemps as there are letters in the word.

Guessed and missed letters will be displayed on the skreen like this

```
Guess a letter:
a
Missed, mistake 3 out of 10

The word: cucumb*r*

Misses: y, k, a
```
At the end you will get an inscription with you result.

### Have a good play!

[travis-url]: https://travis-ci.com/github/Verbarius/Software-architecture
[travis-badge]: https://travis-ci.com/Verbarius/Software-architecture.svg?branch=master
[coverage-image]: https://codecov.io/gh/Verbarius/Software-architecture/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/gh/Verbarius/Software-architecture