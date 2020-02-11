from artwork_catalog import Artist, Artworks
import sqlite3
conn = sqlite3.connect('art_catalog.sqlite')
curr = conn.cursor()

conn.execute('create table if not exists artists (Name txt, Email text, Art_id numeric)')
conn.execute('create table if not exists artwork (Art_id numeric, Artist text, ArtName text, Price numeric, Sold boolean)')

#Prompts user for data imput
def add_artist(name, email, art_id):
    name = input("Enter name of the artist: ")
    email = input("Enter the artist's email: ")
    art_id = int(input("Enter art_id number: "))

    #Add/insert data into a table by using sqlite query
    conn.execute('insert into artists value (?, ?, ?)', (name, email, art_id )) 
    conn.commit()#Tell the database to save the imputs 
    # conn.execute('drop table  artists')
    # conn.commit()

def add_artwork(art_id, artist_name, art_name, price, sold):
    art_id = int(input("enter art_id number: "))
    artist_name = input("Enter the artist name: ")
    art_name = input("Enter the name of the art: ")
    price = float(input("Enter the price of the art: "))

    #Add/insert data into the second table by using sqlite query
    conn.execute('insert into artwork value (?, ?, ?, ?, ? )', (art_id, artist_name, art_name, price, sold)) 
    conn.commit()#Tell the database to save the imputs 
    # conn.execute('drop table  artwork')# I will drop the table when i need it
    # conn.commit()



