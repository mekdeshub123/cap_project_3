from artwork_catalog import Artist

#def add_artist(name, email, art_id):
def add_artist(obj_artist):
    name = input("Enter name of the artist: ")
    email = input("Enter the artist's email: ")
    art_id = int(input("Enter art_id number: "))

    obj_artist = Artist(name, email, art_id)
    
    return f'My Name :{obj_artist.name} and my Email: {obj_artist.email}'

my_result = add_artist('obj')
print(my_result)