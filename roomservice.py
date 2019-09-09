import time

class RoomService:

    def __init__(self, roomstatus):

        self.roomstatus = roomstatus

    def offerDrinks(self): 

        hour = time.strftime('%H')
        hour = int(hour)
        drinks = ['Beer','Wine','Cocktail','Smokey glass sitting at the edge of the bar']
        drinknum = 1

        print('\n')
        print('\n< You take a look around and notice a room with a bar to the left. You decide to walk in. >')
        print('\n')

        if hour > 17:
            print('The bartender says "Time for drinks!"  Whatcha drinkin mate?')
            
            for drink in drinks:
                print(f'{drinknum}. {drink}')
                drinknum = drinknum+1

            select_drink = input('Please enter a number for the drink you wish to have: ')
            select_drink = int(select_drink)
            
            if select_drink == 1:
                print('\n< You enjoy the drink! >')
            elif select_drink == 2:
                print('\n< You enjoy the drink! >')
            elif select_drink == 3:
                print('\n< You enjoy the drink! >')
            elif select_drink == 4:
                print('\n< You start grasping your throat, POISON!!! Unfortunately, you die. The rest of the guests leave >')

        else:
            print('\n')
            print('<There is no one working at the bar right now.  You wonder when someone will show you where your room is.>')