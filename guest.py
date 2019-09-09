class Guest:

    def __init__(self, name):
            
        self.name = name

    def welcome(self):

        print('------------------------------')
        print('Welcome to the Menzie Estates!')
        print('------------------------------')
        print('\n')
        print('We do hope that you enjoy your stay!')
        print('\n')

    def greet_guests(self):

        filename = 'hotelguests.txt'

        print('------------------------------')
        print('Welcome guests:')

        with open(filename) as file_object:
            for line in file_object:
                print(line.strip())
        
        print('------------------------------')



