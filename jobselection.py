import os,sys,time,random
from terminaltables import AsciiTable

typing_speed = 70 #wpm
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

pay1 = 50.00
pay2 = 78.75
pay3 = 145.25

jobselection = 99

prereq1 = 'None'
prereq2 = 'Food Service Mgt I'
prereq3 = '24 Months as Shift Manager'

def jobselect():
    clear()

    print('Welcome to the Job Listings Page')
    jobTable = [
    ['Jobs Available', 'Daily Pay', 'Prerequisites'],
    ['1. ' + job1,'${:,.2f}'.format(pay1),prereq1],
    ['2. ' + job2,'${:,.2f}'.format(pay2),prereq2],
    ['3. ' + job3,'${:,.2f}'.format(pay3),prereq3],
    ]
            
    table = AsciiTable(jobTable)
    print table.table
        
    jobselection = raw_input("Please Enter a Selection or press Enter to go Back: ")
    
    if jobselection == '1':
        choice = raw_input("Are you sure you want Cashier as Your Job? <y/n>: ")
        if choice == 'y':
            slow_type("Congrats Your Application Has been Accepted!")
            slow_type("You will Now Make $56 per Day")
            time.sleep(2)
            jobSel = 1
            clear()
        if choice == 'n':
            jobselect()
        else:
            jobselect()
    if jobselection == '2':
        print('fix me!')
    if jobselection == '3':
        print('fix me!')
    else:
        from mainmenu import mainmenu
        mainmenu()
    