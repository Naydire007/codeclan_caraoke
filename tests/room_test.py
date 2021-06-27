import unittest
from classes.Guest import Guest
from classes.Room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Simone Simons",300)

    def test_add_guest_room(self):
        self.guest1.add_guest(self.guest1)
        self.assertEqual("Simone Simons",self.guest1.add_guest(self.guest1))