#Class created for Artist

class Artist():
    def __init__(self,name, email,):
        #self.artist_id = artist_id
        self.name = name
        self.email = email


class Artworks():
    def __init__(self, art_name, price, sold, artist_id ):
        self.art_name = art_name
        self.price = price
        self.sold = sold
        self.artist_id = artist_id
    # def __str__(self):
    #     return 'Artist_Name: {}, Art_Name: {}, Price:{}, Sold: {}'.format(self.artist_name, self.art_name, self.price, self.sold)
