## Trying filename open / closing, IO, loops and classes
## Eric Menzie 9/8/19

from guest import Guest

filename = 'hotelguests.txt'
the_guest = Guest('')

the_guest.welcome()

with open(filename, 'a') as file_object:
    while True:
        a_guest = input('What is your, or your guest''s, name? (Enter "q" if finished): ')

        if a_guest == 'q':
            break
        else:
            file_object.write(a_guest + "\n")
            print(f'Welcome {a_guest}!')

the_guest.greet_guests()
