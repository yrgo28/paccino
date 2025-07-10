import os
import termcolor
from termcolor import colored

import backend
import func

function = func
program = backend.Options()

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
                sync_menu()
            elif(choose==4):
                more_menu()
            elif(choose==5):
                program.help()

        func.UI().separator("line")
        func.Interact().enter_to_continue()
        main_menu()

def sync_choose():
    cons_avail = ["1", "2"]
    re_cons = input("Type your option: ")
    if(re_cons not in cons_avail):
        if(re_cons=="00"):
            main_menu()

        sync_menu()
    else:
        cons = int(re_cons)
    while True:
        if(cons >= 1 and cons <= 2):
            function.UI().separator("line")
            if(cons==1):
                program.upto("date")
                break;
            elif(cons==2):
                program.upto("grade")
                print(":: AFTER AN UPGRADE, DEVICE REBOOT IS HIGHLY RECOMMENDED ::")
                func.UI().separator("enter")
                break;
        else:
            break;

    func.Interact().enter_to_continue()
    sync_menu()

def sync_menu():
    function.UI().clear()
    function.UI().header("sync")
    function.UI().separator("line")
    print(colored("[1] Databases", "green"))
    print(colored("[2] System Upgrade", "cyan"))
    function.UI().separator("enter")
    print("[00] Back")
    function.UI().separator("line")
    sync_choose()

def more_choose():
    cons_avail = ["1", "2", "3", "4"]
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

        if(choose >= 1 and choose <= 4):
            function.UI().separator("line")
            if(choose==1):
                program.search()
            elif(choose==2):
                program.list()
            elif(choose==3):
                program.cache_clean()
            elif(choose==4):
                program.autoclean()
            
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
    print(colored("[3] Cache Clean", "cyan"))
    print(colored("[4] Remove Unused", "red"))
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
    print(colored("[3] Synchronize", "blue")) #UPDATE > UPGRADE
    print(colored("[4] More", "yellow")) #SEARCH > LIST > CACHE CLEAN > AUTOREMOVE
    print(colored("[5] Help", "magenta"))
    function.UI().separator("enter")
    print("[00] Quit")
    function.UI().separator("line")
    menu_choose()

main_menu()
