from gallow_play import Gallow, word_for_guess


if __name__ == '__main__':
    word = word_for_guess()
    play = Gallow(word)
    play.gallow()
