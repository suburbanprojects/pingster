#import ping3 module
from ping3 import ping, verbose_ping
#import cool ascii art text stuff
from termcolor import colored
from pyfiglet import Figlet

#this function pings once, if address is online will show true
def oneping(addr):
    resp=ping(addr) 

    if resp == False:
        return False
    else:
        return True

#this function pings according to the times provided by the user
def multiping(addr):
    verbose_ping(addr, count=attempts)

#show menu
f = Figlet(font='slant')
print(colored(f.renderText('Pingster'), 'yellow'))
print("------Select function------")
print("| 1. Ping once            |")
print("| 2. Ping multiple times  |")
print("---------------------------")


while True:
    #take input from user
    choice = input("Enter choice(1/2): ")
    
    if choice in ("1", "2"):
        addr=input("Enter address to ping: ")

    if choice == '1':
        print(colored(oneping(addr),'green'))

    elif choice == '2':
        attempts=int(input("Ping how many times: "))
        print(multiping(addr))

    #ask if they want to continue the program, if not, break the loop and quit the program
    next_question = input("Try again? (yes/no): ")
    if next_question == "no":
        break

else:
    print("Invalid input")

        
        
