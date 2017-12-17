import os,sys,time,random
from terminaltables import AsciiTable

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

# Variable Initialization

clear = lambda: os.system('cls')

job1 = 'Cashier'
job2 = 'Shift Manager'
job3 = 'Store Manager'

pay1 = 8.00
pay2 = 11.25
pay3 = 20.75

jobsel = 99

prereq1 = 'None'
prereq2 = 'Food Service Mgt I'
prereq3 = '24 Months as Shift Manager'

def jobselect():
    clear()

    print('Welcome to the Job Listings Page')
    jobTable = [
    ['Jobs Available', 'Hourly Pay', 'Prerequisites'],
    ['1. ' + job1,'${:,.2f}'.format(pay1),prereq1],
    ['2. ' + job2,'${:,.2f}'.format(pay2),prereq2],
    ['3. ' + job3,'${:,.2f}'.format(pay3),prereq3],
    ]
            
    table = AsciiTable(jobTable)
    print table.table
        
    jobsel = raw_input("Please Enter a Selection or press Enter to go Back: ")
    
    if jobsel == [1,2,3]:
        jobsel()
    else:
        from mainmenu import mainmenu
        mainmenu()
    
def jobsel():
    if jobsel == 1:
        choice = raw_input("Are you sure you want Cashier as Your Job? <y/n>: ")
        if choice == 'y':
            slow_type("Congrats Your Application Has been Accepted!")
            slow_type("We just need to fill out some paper work")
            clear()
        if choice == 'n':
            jobselect()
        else:
            print("Not A valid answer! Please enter y or n!")
            jobsel()
    if jobsel == 2:
        print('fix me!')
    if jobsel == 3:
        print('fix me!')
    
