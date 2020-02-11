#Class created for Artist

class Artist():
    def __init__(self, name, email, art_id):
        self.name = name
        self.email = email
        self.art_id = art_id


class Artworks():
    def __init__(self, art_id, artist_name,art_name, price, sold=False ):
        self.art_id = art_id
        self.artist_name = artist_name
        self.art_name = art_name
        self.price = price
        self.sold = sold
    # def __str__(self):
    #     return 'Artist_Name: {}, Art_Name: {}, Price:{}, Sold: {}'.format(self.artist_name, self.art_name, self.price, self.sold)
