
from artwork_db import *  
 
def main():


    #user function choices
    print('\n')
    print('A = add new artist')
    print('AW = to add new artwork ')
    print('S = search all art work by artist_name')
    print('V = to display avaliable art work by artist')
    print('D = delete an art-work')
    print('U = to update avaliability status')
    print("\n")
   
        #Call all of the functions and put them in try block
    try:
        function_choice = input("Enter your choice of function: ")
        choice = function_choice.upper()
        if choice == 'A':
            add_artist('obj_artist') 
        #    ans = add_artist('obj_artist') # Call the add function
        #    print(f'{ans} row added!')
        elif choice == 'AW':
            add_artwork('obj_artwork')

        elif choice == 'S':
            search_artwork_by_artist_name('obj_artist_name')   
                
        elif choice == 'V':
            display_avaliable_artwork_by_artist('obj_avaliable_artwork')

        elif choice == 'U':
            update_avaliability('obj_art_name')

        elif choice == 'D':
            delete_artwork('obj_art_delete')       

        else:
            print("wrong selection")
    except:
        print("error")
    #finally:
if __name__ == "__main__":
    main()