from terminaltables import AsciiTable
from colorama import init, Fore, Style
import os

init(convert = True)

clear = lambda: os.system('cls')

option1 = Style.BRIGHT + Fore.WHITE + 'Enter 1 For Gang Menu'
option2 = 'Enter 2 For Weapon Dealer'
option3 = 'Enter 3 For Heists Menu'
option4 = 'Enter 4 For Safehouse Menu' + Style.RESET_ALL

def Dmenu():
    clear()
    print('Welcome to the Dark Side')

    
    darkTable = [
    [Fore.RED + 'Health', Fore.GREEN + 'Cash', Fore.RED + 'Reputaion', 'Wanted Level' + Style.RESET_ALL],
    ]
    
    table = AsciiTable(darkTable)
    print table.table
    

    print(option1)
    print(option2)
    print(option3)
    print(option4)
    
    raw_input('Enter: ')
    
Dmenu()