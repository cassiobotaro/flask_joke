from unittest import TestCase

import flask_joke


def test_is_string():
    s = flask_joke.joke()
    assert isinstance(s, str)


def test_joke_content():
    s = flask_joke.joke()
    s == '<p>Wenn ist das Nunstück git und Slotermeyer? Ja! ... <strong>Beiherhund</strong> '
    'das Oder die Flipperwaldt gersput.</p>'


# for historical reasons
# class TestJoke(TestCase):

#     def test_is_string(self):
#         s = flask_joke.joke()
#         self.assertTrue(isinstance(s, str))

#     def test_joke_content(self):
#         s = flask_joke.joke()
#         self.assertTrue(s, '<p>Wenn ist das Nunstück git und Slotermeyer? Ja! ... <strong>Beiherhund</strong> '
#                 'das Oder die Flipperwaldt gersput.</p>')
