# Importing libs
import platform
import os
import time

print('''By MINIGO Germany GmbH / Limetable''')
print('''██████╗ ██╗      █████╗ ██████╗ ████████╗███████╗ ██████╗ ██████╗ ███╗   ███╗██╗███████╗██╗   ██╗
██╔══██╗██║     ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗████╗ ████║██║██╔════╝╚██╗ ██╔╝
██████╔╝██║     ███████║██████╔╝   ██║   █████╗  ██║   ██║██████╔╝██╔████╔██║██║█████╗   ╚████╔╝ 
██╔═══╝ ██║     ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██║██╔══╝    ╚██╔╝  
██║     ███████╗██║  ██║██║  ██║   ██║   ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║██║        ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝        ╚═╝   
                                                                                                 ''')

print('Maintained by MiniGo DEV Group')

print('---->\n'
      'os : shows os info \n'
      'pc : shows PC info\n'
      '<----\n')
print('what do you want to see?')
f = input("Enter: ")

if f == "os":
    print('OS: ', platform.system())
    print('Version: ', platform.release())
    print('----> Python')
    print('Python version: ', platform.python_version())
    time.sleep(60)

elif f == "pc":
    print('Machine: ', platform.machine())
    print('Processor: ',platform.processor())
    time.sleep(60)
else:
    print('try again!')
