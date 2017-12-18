from colorama import init, Fore, Style, Back
import os
init(convert = True)
clear = lambda: os.system('cls')


def shopmenu():
    clear()
    print(Style.BRIGHT + Back.WHITE + Style.NORMAL + Fore.BLACK + 'Welcome To the Shopping Menu!' + Style.RESET_ALL)
    print('1. Schnucks Grocery Store')
    print('2. JiffyLube Car TuneUP and Gas')
    print('3. Your Local Car Dealer')
    print('4. Joes Department Store')
    
    shopselect = int(raw_input('Please make a selection: '))
    
    if shopselect == 1:
        grocery()
    if shopselect == 2:
        tuneup()
    if shopselect == 3:
        cardealer()
    if shopselect == 4:
        departmentstore()
    else:
        shopmenu()
        
def grocery():
    clear()
    print(Style.BRIGHT + Back.WHITE + Style.NORMAL + Fore.BLACK + 'Welcome To Schnucks' + Style.RESET_ALL)
    mealamt = int(raw_input('\nHow many Meals would you like to buy? or Press enter to go back: '))
    
    mealcost = mealamt * 2
    
    try:
        if mealamt > 0:
            ans = raw_input('Are you sure you want to purchase ' + str(mealamt) + ' for ' + '$' + str(mealcost) + '? <y/n>: ')
            if ans == 'y':
                from mainmenu import money, meals
                if money > mealcost:
                    money -= mealcost
                    meals += int(mealamt)
                    shopmenu()
            if ans == 'n':
                grocery()
                
            else:
                raw_input('You do not have enough money, press enter to go back: ')
                grocery()
        else:
            grocery()
    except ValueError:
        shopmenu()

    
    