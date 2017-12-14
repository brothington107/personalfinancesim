from terminaltables import AsciiTable

def mainmenu():
    mainStats = [
    ['\033[1;32;40mMoney', 'Health'],
    ['$100', '%100'],
    ]
    table = AsciiTable(mainStats)
    print table.table