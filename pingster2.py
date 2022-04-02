import platform  # Get the operating system name
import subprocess # To execute  shell command
from pyfiglet import Figlet #import ascii art stuff

#both functions will return true if the address responds to the ping request

#this function will ping the given address once
def oneping(addr): 
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command to ping once. Ex: "ping -c 1 addr"
        command = ['ping', parameter,'1',addr]
        response = subprocess.call(command)

        if response ==  0:
            return True
        else:
            return False
        
#this function will ping the  address multiple times, following value provided by user
def multiping(addr): 
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command to ping multimetimes. Ex: "ping -c times addr"
        command = ['ping', parameter,times,addr]
        response = subprocess.call(command)

        if response ==  0:
            return True
        else:
            return False

 #show menu       
f = Figlet(font='digital')
print(f.renderText('Pingster 2'))
print("=======Select  function=======")
print("    1. Ping once               ")
print("    2. Ping multiple times     ")
print("    3. Quit                    ")
print("="*30 )

while True:
    #take input from user
    choice = input("Enter choice(1/2/3): ")
    
    if choice in ("1", "2"):
        addr=input("Enter address to ping: ")

    if choice == '1':
        print(oneping(addr))

    if choice== '2':
        times=input("Ping how many times: ")
        print(multiping(addr))

    #quits the program
    if choice=='3':
        break
