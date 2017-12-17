from terminaltables import AsciiTable
from jobselection import jobselect
from colorama import init, Fore, Style
import os

init(convert = True)

clear = lambda: os.system('cls')

# Variable Initialization
option1 = Style.BRIGHT + Fore.WHITE + 'Enter 1 For Job Selection'
option2 = 'Enter 2 For Shopping'
option3 = 'Enter 3 For ATM'
option4 = 'Enter 4 For Bill Payment'
option5 = 'Enter 5 For Housing Options' + Style.RESET_ALL

money = 5000
health = 100
meals = 6
month = 'January'
day = 1

def mainmenu():
    clear()
    print('Welcome to the Main Menu!')
    print("Tip: You need 2 Meals Per Day")

    mainTable = [
    [Style.BRIGHT + Fore.GREEN + 'Net Worth' + Style.RESET_ALL, Style.BRIGHT + Fore.RED + 'Health' + Style.RESET_ALL, Style.BRIGHT + Fore.YELLOW + 'Meals' + Style.RESET_ALL , 'Month', 'Day'],
    ['${:,.2f}'.format(money), health, meals, month, day],
    ]
    
    table = AsciiTable(mainTable)
    print table.table
    menuselect()
    
def menuselect():
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    print(option5)

    menusel = int(raw_input("Please make a selection: "))
    
    if menusel == 1:
        jobselect()
    else:
        print('Error Please Enter a Valid Selection')
        raw_input("Press enter to continue...")
        menuselect()    