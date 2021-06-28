class Song:
    def __init__(self,song_name):
        self.song_name = song_name
        self.song_list = []
        # self.song_dict = {
        # {
        #     "artist": "Dan Vasc",
        #     "song1": "Toss a coin to your witcher",
        #     "song2": "The song of the white wolf"
        # },
        # {
        #     "artist": "Manowar",
        #     "song1": "Warriors of the world",
        #     "song2" : "Die for metal"
        # },
        # {   "artist": "Epica",
        #     "song1": "Beyond the matrix",
        #     "song2": "Abyss of Time"

        # }
        # }

        self.song_dict = {
            "Song1": "Toss a coin to your witcher",
            "Song2": "Warriors of the world",
            "Song3": "Beyond the matrix"
        }

    def dictionary(self):
        for song in self.song_dict:
            return song["song1"]
       
       
    
