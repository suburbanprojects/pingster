import platform  # Get the operating system name
import subprocess # To execute  shell command
from pyfiglet import Figlet #import ascii art stuff

def multiping(addr): 
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command to ping multimetimes. Ex: "ping -c times addr"
        command = ['ping', parameter,times,addr]
        response = subprocess.call(command)

        if response ==  0:
            return True
        else:
            return False

def pingsweep(addr):
    for i in range(start,end):
        host = addr + str(i) # store the ip in host variable while in loop
        parameter = '-n' if platform.system().lower()=='windows' else '-c' 
        #hide the detail of the ping output
        parameter2 = ' nul' if platform.system().lower()=='windows' else ' /dev/null'
        # Building the command to ping sweep. Ex: "ping -c 1 -w 1 addr host >nul"
        command = ['ping', parameter, '1', '-w 1', addr, host]
        response = subprocess.call(command, stdout=open(parameter2, 'w'), stderr=subprocess.STDOUT) #take the command and display output to console
    
        if response == 0:
            print(host + " is up")
        else:
            print(host + " is down")
            
f = Figlet(font='slant')
print(f.renderText('Pingster'))
print("=======Select  function=======")
print("|    1. Ping an IP           |")
print("|    2. Perform Ping Sweep   |")
print("|    3. Quit                 |")
print("="*30 )


while True:
    choice = input("Enter choice(1/2/3): ")

    if choice in ("1"):
        addr=input("Enter address to ping: ")
        times=input("Ping how many times: ")
        print(multiping(addr))

    if choice== '2':
        #enter IP address here
        addr = input("Enter IP address: ")
        dot = addr.rfind(".") #rfind extracts the index of the last occurrence of the decimal point
        addr = addr[0:dot + 1] #and the value is stored in dot
        #enter range here
        start = int(input("Enter start range (min value 0): "))
        end = int(input("Enter end range (max value 255): "))
        print(pingsweep(addr))

    if choice=='3':
        break
