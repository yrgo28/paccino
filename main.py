import os
import termcolor
from termcolor import colored

import backend
import func
import autostart

function = func
program = backend.Options()

def start_options():
    avail = ["1", "2"]
    cons = input("Start as: ")

    if(cons=="99"):
        print("Paccino need to be restarted.")
        autostart = input('Autostart option: ')

        if(autostart in avail):
            autostart = int(autostart)
        else:
            start_menu()

        if(autostart >= 1 and autostart <= 2):
            pass
        else:
            start_menu()
        
        comm = 'sudo echo "AUTOSTART_IS=' + str(autostart) + '" > $PACCINO_PATH/autostart.py'
        func.Interact()._exec(comm)
        

    if(cons=="00"):
        func.UI().clear()
        exit()

    if(cons in avail):
        choose = int(cons)
    else:
        start_menu()

    while True:
        if(choose >= 1 and choose <= 2):
            if(choose==1):
                func.Interact()._exec("python3 $PACCINO_PATH/secure_mode.py")
            elif(choose==2):
                main_menu()
        else:
            start_menu()

        break;

def start_menu():
    func.UI().clear()
    func.UI().header("start")
    func.UI().separator("line")
    print(colored("[1] Secure Mode", "blue"))
    print("info: Minor risk for bugs & more safety.")
    func.UI().separator("enter")
    print(colored("[2] Normal Mode", "magenta"))
    print("info: More options, but take your own risk.")
    func.UI().separator("enter")
    print(colored("[99] Set autostart", "green"))
    func.UI().separator("enter")
    print("[00] Quit")
    func.UI().separator("line")
    start_options()


def printthisis(arg: str):
    print('this is ' + arg + ' option')
    cons = input("press [enter] to continue...")
    #USED FOR DEBUG

def menu_choose():
    cons_avail = ["1", "2", "3", "4", "5"]
    cons_choose = input("Type your option: ")
    choose: int

    if(cons_choose not in cons_avail):
        if(cons_choose=="00"):
            func.UI().clear()
            exit()
        main_menu()
    else:
        choose = int(cons_choose)

    while True:
        if(choose >= 1 and choose <= 5):
            if(choose==1):
                program.install()
            elif(choose==2):
                program.remove()
            elif(choose==3):
                program.upgrade()
            elif(choose==4):
                more_menu()
            elif(choose==5):
                program.help()

        func.UI().separator("line")
        func.Interact().enter_to_continue()
        main_menu()

def more_choose():
    cons_avail = ["1", "2", "3", "4", "5"]
    cons_input = input("Type your option: ")
    if(cons_input not in cons_avail):
        if(cons_input=="00"):
            main_menu()
        more_menu()
    else:
        choose = int(cons_input)
    while True:
        if(choose<=0):
            main_menu()

        if(choose >= 1 and choose <= 5):
            function.UI().separator("line")
            if(choose==1):
                program.search()
            elif(choose==2):
                program.list()
                more_menu()
            elif(choose==3):
                program.cache_clean()
            elif(choose==4):
                program.autoclean()
            elif(choose==5):
                program.revert()
            
            function.UI().separator("line")
            function.Interact().enter_to_continue()
        else:
            break;
        break;

    more_menu()

def more_menu():
    function.UI().clear()
    function.UI().header("more")
    function.UI().separator("line")
    print(colored("[1] Search", "green"))
    print(colored("[2] List Installed", "yellow"))
    print(colored("[3] Cache Clean", "red"))
    print(colored("[4] Remove Unused", "magenta"))
    print(colored("[5] Revert Update/Install From File", "blue"))
    function.UI().separator("enter")
    print("[00] Back")
    function.UI().separator("line")
    more_choose()

def main_menu():
    function.UI().clear()
    function.UI().header("main")
    function.UI().separator("line")
    print(colored("[1] Install", "green"))
    print(colored("[2] Remove", "red"))
    print(colored("[3] Synchronize", "blue")) #sudo pacman -Syu
    print(colored("[4] More", "yellow")) #SEARCH > LIST > CACHE CLEAN > AUTOREMOVE > REVERT UPDATE
    print(colored("[5] Help", "magenta"))
    function.UI().separator("enter")
    print("[00] Quit")
    function.UI().separator("line")
    menu_choose()

#PACCINO LAUNCH
if(autostart.AUTOSTART_IS==1):
    func.Interact()._exec("python3 #PACCINO_PATH/secure_mode.py")
elif(autostart.AUTOSTART_IS==2):
    main_menu()
else:
    start_menu()

