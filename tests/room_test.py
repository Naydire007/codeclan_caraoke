from classes.Song import Song
import unittest
from classes.Guest import Guest
from classes.Room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Wings of Freedom",10)
        self.song1 = Song("Beyond the matrix")
        self.guest1 = Guest("Simone Simons",300, "Beyond the matrix")

    def test_room_has_name(self):
        self.assertEqual("Wings of Freedom", self.room.room_name)
    
    def test_add_guest(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(1, self.room.count_guests())
    
    def test_remove_guest(self):
        self.room.remove_guest(self.guest1)
        self.assertEqual(0,self.room.count_guests())

    def test_add_song_room(self):
        self.room.add_song(self.song1)
        self.assertEqual(1,self.room.count_song())

    def test_room_space(self):
        self.room.add_guest(self.guest1)
        self.room.room_space(self.room.count_guests)
        self.assertEqual(1,self.room.count_guests())

    def test_room_space_VIP(self):
        self.room.add_guest(self.guest1)
        self.room.room_space_VIP(self.room.count_guests)
        self.assertEqual(1,self.room.count_guests())

    def test_customer_pays_entry(self):
        self.guest1.pay_entry(10)
        self.assertEqual(290,self.guest1.wallet)