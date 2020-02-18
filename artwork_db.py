from artwork_catalog import Artist, Artworks
import sqlite3
conn = sqlite3.connect('art_catalog.sqlite')
cur = conn.cursor()

conn.execute('create table if not exists artists (Artist_Id integer PRIMARY KEY autoincrement, Name txt, Email text)')
conn.execute('create table if not exists artwork ( Art_Name text UNIQUE, Price numeric, Sold text, Artist_Id integer, Foreign key (Artist_id) REFERENCES artists(Artist_Id))')
conn.execute('PRAGMA foreign_keys = ON')

#Prompts user for data imput
#def add_artist(name, email, art_id):
def add_artist(obj_artist):
    name = input("Enter name of the artist: ")
    email = input("Enter the artist's email: ") 

    obj_artist = Artist(name, email,)

    #Add/insert data into a table by using sqlite query
    row=conn.execute('insert into artists (Name, Email) values (?, ? )', (obj_artist.name.upper(), obj_artist.email )) 
    
    conn.commit()#Tell the database to save the imputs 
    # conn.execute('drop table  artists')
    # conn.commit()
    return row.rowcount

def add_artwork(obj_artwork): #function
    art_name = input("Enter the name of the art: ")
    price = float(input("Enter the price of the art: "))
    sold = input("Is the art avaliable? enter avaliabl or sold: ")
    artist_id = int(input("Enter artist id: "))
    obj_artwork = Artworks( art_name, price, sold, artist_id)

    #Add/insert data into the second table by using sqlite query
    conn.execute('insert into artwork values (?, ?, ?, ? )', (obj_artwork.art_name.upper(), obj_artwork.price, obj_artwork.sold, obj_artwork.artist_id)) 
    conn.commit()#Tell the database to save the imputs 
    #conn.execute('drop table  artwork')# I will drop the table when i need it
    #conn.commit()
    
def search_artwork_by_artist_name(obj_artist_Id):#passing parameter
    search_Id = int(input("Enter artist Id: "))
    # obj_artist_name = Artworks(1, search_name, "mekdes", 0, "sold")
    obj_artist_Id = Artworks("art_name", 1, "sold",search_Id )
    search_artwork_sql = 'SELECT Artists.name, Artwork.art_name, Artwork.price, Artwork.sold, Artwork.artist_Id FROM Artists JOIN Artwork ON Artists.artist_Id = Artwork.artist_Id WHERE Artists.artist_Id = ?'
    cur.execute(search_artwork_sql,(obj_artist_Id.artist_id, ))
    rows = cur.fetchall()
    print(rows)
    # for row in rows:
    #     print(row)

def display_avaliable_artwork_by_artist(obj_avaliable_artwork):
    avaliable_art = ("Enter the artist name to search avaliable work: ")
    obj_avaliable_artwork = Artworks("art_name", 1, avaliable_art, 1 )
    avaliable_artwork_sql = 'SELECT * From Artists INNER JOIN Artists ON Artwork.Artist_Id = ?'
    cur.execute(avaliable_artwork_sql, (obj_avaliable_artwork.sold))
    rows = cur.fetchall()
    print(rows)

def update_avaliability(obj_art_name):
    name_of_art = input("Enter the name of the art: ")
    avaliability = input("Update status: ")
    obj_art_name = Artworks(name_of_art, 1, avaliability, 1)
    name_of_art_sql = 'UPDATE artwork SET Sold = ? WHERE art_name = ?'
    cur.execute(name_of_art_sql, (obj_art_name.art_name, obj_art_name.sold))
    conn.commit()
    rows = cur.rowcount
    print(rows)

def delete_artwork(obj_art_delete):
    delete_art_name = input("Enter the art name: ")
    obj_art_delete = Artworks(delete_art_name, 1, "sold", 1)
    obj_art_delete.art_name=delete_art_name
    delete_art_name_sql = 'DELETE FROM artwork WHERE art_name = ?'
    cur.execute(delete_art_name_sql, (obj_art_delete.art_name, ))
    conn.commit
    rows = cur.rowcount
    print(rows)
    

#if __name__ == "__main__":# Calling the main function
   #add_artwork('object_artwork').lower()
   #search_artwork_by_artist_name('obj_artist_name')
   #add_artist('obj_artist').lower()# Call the add function
   #update_avaliability('obj_art_name').lower()

#     #user function choices
#     print('\n')
#     print('A = add new artist')
#     print('AW = to add new artwork ')
#     print('S = search all art work by artist_name')
#     print('V = to display avaliable art work by artist')
#     print('D = delete an art work')
#     print('U = to update avaliability status')
#     print("\n")
    
#         #Call all of the functions and put them in try block
#     try:
#         function_choice = input("Enter your choice of function: ")
#         choice = function_choice.upper()
#         if choice == 'A': 
#             add_artist('obj_artist') # Call the add function

#         elif choice == 'AW':
#             add_artwork('object_artwork')

#         elif choice == 'S':
#             search_artwork_by_artist_name('obj_artist_name')   
                
#         elif choice == 'V':
#             display_avaliable_artwork_by_artist('obj_avaliable_artwork')

#         elif choice == 'U':
#             update_avaliability(obj_art_name)

#         elif choice == 'D':
#             delete_artwork(obj_art_delete)
#             #delete_artwork('obj_art_name')
        

#         # elif function_choice == 'C':
#         #      update_avaliability('obj_art_name')

#         else:
#             print("wrong selection")
#     except:
#         print("error")
# #finally: