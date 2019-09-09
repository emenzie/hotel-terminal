## Trying filename open / closing, IO, loops and classes
## Eric Menzie 9/8/19
## Hotel game

from guest import Guest
from roomservice import RoomService

filename = 'hotelguests.txt'
the_guest = Guest('')
call_roomservice = RoomService('')

the_guest.welcome()

with open(filename, 'a') as file_object:
    while True:
        a_guest = input('What is your, and your guest''s, names? (Enter "q" if finished): ')

        if a_guest == 'q':
            break
        else:
            file_object.write(a_guest + "\n")
            print(f'Welcome {a_guest}!')

the_guest.greet_guests()
call_roomservice.offerDrinks()
