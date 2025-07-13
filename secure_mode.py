import os
import termcolor
from termcolor import colored

import func

ui = func.UI()
interact = func.Interact()

def choose():
    avail = ["1", "2", "3"]
    cons = input('Type your option: ')
    choose: int
    
    if(cons=="00"):
        ui.clear()
        exit()

    if(cons=="99"):
        comm = 'sudo echo "AUTOSTART_IS=None" > $PACCINO_PATH/autostart.py'
        interact._exec(comm)
        ui.separator("line")
        interact.enter_to_continue()

    if(cons in avail and cons != None):
        choose = int(cons)
    else:
        menu()

    while True:
        if(choose >= 1 and choose <= 3):
            if(choose==1):
                package = input('Package to install: ')
                if(package != None and len(package) > 1):
                    ui.separator("line")
                    comm = 'sudo pacman -Sy ' + package
                    interact._exec(comm)
                    break;
                else:
                    break;
            elif(choose==2):
                package = input('Package to remove: ')
                if(package != None and len(package) > 1):
                    ui.separator("line")
                    comm = 'sudo pacman -R ' + package
                    interact._exec(comm)
                    break;
                else:
                    break;
            elif(choose==3):
                ui.separator("line")
                interact._exec("sudo pacman -Syu")
                ui.separator("enter")
                print("info: after an update, reboot is highly recommended.")
                break;
            else:
                break;

    ui.separator("line")
    interact.enter_to_continue()
    menu()


def menu():
    ui.clear()
    ui.header("secure-mode")
    ui.separator("line")
    print(colored("[1] Synchronize & Install", "green"))
    print(colored("[2] Remove", "red"))
    print(colored("[3] Synchronize", "cyan"))
    ui.separator("enter")
    print(colored("[99] Reset autostart", "blue"))
    print("[00] Quit")
    ui.separator("line")
    choose()

menu()

