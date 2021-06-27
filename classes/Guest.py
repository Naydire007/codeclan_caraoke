class Guest:
    def __init__(self,name,wallet,favorite_song):
        self.name = name
        self.wallet = wallet
        favorite_song = favorite_song
       

    def pay_entry(self,room):
        self.wallet -= room.price

    def pay_entry_VIP(self,room):
        self.wallet -= room.VIP_price
  
        

    
        