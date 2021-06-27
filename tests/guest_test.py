from classes.Room import Room
import unittest
from classes.Guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
      self.guest = Guest("Simon Simons", 200, "Beyond the matrix")
        

    def test_guest_name(self):
      self.assertEqual("Simon Simons",self.guest.name)

    