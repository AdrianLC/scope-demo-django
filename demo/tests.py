import unittest

from demo.tasks import hello_world


class UnitTests(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")
