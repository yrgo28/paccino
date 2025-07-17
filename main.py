import os
import termcolor
from termcolor import colored

import backend
import func
import autostart

function = func
program = backend.Options()

def set_autostart(to):
    comm = 'sudo echo "AUTOSTART_IS=' + str(to) + '" > $PACCINO_PATH/autostart.py'
    func.Interact()._exec(comm)

def start_options():
    avail = ["1", "2"]
    cons = str(input("Start as: "))

    if(cons=="99"):
        print(colored("info: restart required.", "magenta"))
        autostart = input('Autostart: ')

        if(autostart in avail):
            autostart = int(autostart)
        else:
            start_menu()

        if(autostart >= 1 and autostart <= 2):
            pass
        else:
            start_menu()
        
        set_autostart(str(autostart)) 

    if(cons=="00"):
        func.UI().clear()
        exit()

    while True:
        if(cons == "1" or cons == "2"):
            if(cons=="1"):
                func.Interact()._exec("python3 $PACCINO_PATH/secure_mode.py")
                exit()
            elif(cons=="2"):
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
    print(colored("[99] Set Autostart Option", "green"))
    print("[00] Quit")
    func.UI().separator("line")
    start_options()

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
    cons_avail = ["1", "2", "3", "4", "5", "6", "7"]
    cons_input = input("Type your option: ")

    if(cons_input not in cons_avail):
        if(cons_input=="00"):
            main_menu()
        elif(cons_input=="99"):
            func.UI().separator("line")
            set_autostart("None")
            func.Interact().enter_to_continue()

        more_menu()

    else:
        choose = int(cons_input)
    while True:

        if(choose<=0):
            main_menu()

        if(choose >= 1 and choose <= 7):
            function.UI().separator("line")
            if(choose==1):
                program.search()
            elif(choose==2):
                program.search_installed()
            elif(choose==3):
                program.list()
                more_menu()
            elif(choose==4):
                program.cache_clean()
            elif(choose==5):
                program.autoclean()
            elif(choose==6):
                program.revert()
            elif(choose==7):
                function.Interact()._exec("python3 $PACCINO_PATH/opt_manager.py")
                exit()
            
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
    print(colored("[1] Search in Database", "green"))
    print(colored("[2] Search in Packages", "cyan"))
    print(colored("[3] List Packages", "yellow"))
    print(colored("[4] Cache Clean", "magenta"))
    print(colored("[5] Remove Unused", "magenta"))
    print(colored("[6] Install From File", "blue"))
    print(colored("[7] (EXPERIMENTAL) Install '.tar' File", "blue"))
    function.UI().separator("enter")
    print(colored("[99] Reset autostart", "green"))
    print("[00] Back")
    function.UI().separator("line")
    more_choose()

def main_menu():
    function.UI().clear()
    function.UI().header("main")
    function.UI().separator("line")
    print(colored("[1] Install", "green"))
    print(colored("[2] Remove", "magenta"))
    print(colored("[3] Synchronize", "cyan")) #sudo pacman -Syu
    print(colored("[4] More", "yellow")) #SEARCH > LIST > CACHE CLEAN > AUTOREMOVE > REVERT UPDATE
    print(colored("[5] Help", "yellow"))
    function.UI().separator("enter")
    print("[00] Quit")
    function.UI().separator("line")
    menu_choose()

#PACCINO LAUNCH

if(autostart.AUTOSTART_IS==1):
    func.Interact()._exec("python3 $PACCINO_PATH/secure_mode.py")
    exit()
elif(autostart.AUTOSTART_IS==2):
    main_menu()
else:
    start_menu()

