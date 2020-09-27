import unittest
from gallow_play import Gallow, word_for_guess


class TestGame(unittest.TestCase):

    def test_file(self):
        with open('gallow_play/words_.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        word = word_for_guess()
        self.assertEqual(word in lines, True)

    def test_func(self):
        word = 'abracadabra'
        play = Gallow(word)
        play.decision('a')
        self.assertEqual(('').join(play.guessed), 'a**a*a*a**a')
        self.assertEqual(play.mistakes, 0)
        self.assertEqual(', '.join(play.misses), '')
        play.decision('l')
        self.assertEqual(('').join(play.guessed), 'a**a*a*a**a')
        self.assertEqual(play.mistakes, 1)
        self.assertEqual(', '.join(play.misses), 'l')
        play.decision('6')
        self.assertEqual(('').join(play.guessed), 'a**a*a*a**a')
        self.assertEqual(play.mistakes, 1)
        self.assertEqual(', '.join(play.misses), 'l')
        play.decision('br')
        self.assertEqual(('').join(play.guessed), 'a**a*a*a**a')
        self.assertEqual(play.mistakes, 1)
        self.assertEqual(', '.join(play.misses), 'l')
        play.decision('e')
        self.assertEqual(('').join(play.guessed), 'a**a*a*a**a')
        self.assertEqual(play.mistakes, 2)
        self.assertEqual(', '.join(play.misses), 'l, e')
        play.decision('b')
        self.assertEqual(('').join(play.guessed), 'ab*a*a*ab*a')
        self.assertEqual(play.mistakes, 2)
        self.assertEqual(', '.join(play.misses), 'l, e')
