from classes.Song import Song
from classes.Guest import Guest


class Room:
    def __init__(self,room_name):
        self.room_name = room_name
        self.guest_list = []
        self.songs_list = []
        # self.room1 = room1
        # self.room1 = []
        # self.song_list_room1 = []
        # self.room2 = room2
        # self.song_list_room2 = []
        # self.room3 = room3
        # self.song_list_room3 = []
        # self.VIP = VIP
        # self.song_list_VIP = []
       
        # self.room_limit = 6
        # self.VIP_limit = 14
        self.room_price = 10
        self.VIP_price = 20

    def add_guest(self,guest):
        self.guest_list.append(guest)
    
    def remove_guest(self,guest):
        self.add_guest(guest)
        self.guest_list.remove(guest)
 
    def count_guests(self):
        return len(self.guest_list)
 
    def count_song(self):
        return len(self.songs_list)

    def add_song(self,song):
        self.songs_list.append(song.dictionary)

    # def add_song(self):
    #     self.songs_list.append(Song["music"]["song1"]["Beyond the matrix"])