import sys,time,random
from terminaltables import AsciiTable


print(" 888888ba                                                        dP ")
print(" 88    `8b                                                       88")
print("a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. 88d888b. .d8888b. 88")
print(" 88        88ooood8 88'  `88 Y8ooooo. 88'  `88 88'  `88 88'  `88 88 ")
print(" 88        88.  ... 88             88 88.  .88 88    88 88.  .88 88")
print(" dP        `88888P' dP       `88888P' `88888P' dP    dP `88888P8 dP ")
print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
print("                                                                    ")
print(" 88888888b oo                                              ")
print(" 88                                                        ")
print("a88aaaa    dP 88d888b. .d8888b. 88d888b. .d8888b. .d8888b. ")
print(" 88        88 88'  `88 88'  `88 88'  `88 88'  `"" 88ooood8 ")
print(" 88        88 88    88 88.  .88 88    88 88.  ... 88.  ... ")
print(" dP        dP dP    dP `88888P8 dP    dP `88888P' `88888P' ")
print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
print("                                                           ")
print(".d88888b  oo                     dP            dP                     ")
print("88.     '                        88            88                     ")
print(" Y88888b. dP 88d8b.d8b. dP    dP 88 .d8888b. d8888P .d8888b. 88d888b. ")
print("      `8b 88 88'`88'`88 88    88 88 88'  `88   88   88'  `88 88'  `88 ")
print("d8'   .8P 88 88  88  88 88.  .88 88 88.  .88   88   88.  .88 88       ")
print(" Y88888P  dP dP  dP  dP `88888P' dP `88888P8   dP   `88888P' dP       ")
print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

name = raw_input("\nPlease Type A Name: ")

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ''

slow_type("\nWelcome " + name + ".")

slow_type("Lets Get Started!")

mainmenu()
