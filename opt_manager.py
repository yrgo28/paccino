import os
import termcolor
from termcolor import colored

import func

ui = func.UI()
interact = func.Interact()

def extract(arg: str, file: str):
    ui.separator("enter")
    print(colored("info: leave blank to cancel", "yellow"))
    ui.separator("enter")
    target_directory = input("Type directory name to extract: ")
    all_good = False

    if(len(target_directory) > 2):
        all_good = True
        pass #COMPROBAR SI EL USUARIO QUIERE CONTINUAR CON LA EXTRACCION
    else:
        menu()
    
    if(all_good):
        interact._exec('sudo mkdir /opt/' + target_directory)
        ui.separator("line")
    else:
        menu()

    if(arg=="tar.gz"):
        interact._exec('sudo tar -xvzf ' + file + ' -C /opt/' + target_directory)
        ui.separator("line")
    elif(arg=="tar.xz"):
        interact._exec('sudo tar -xf ' + file + ' -C /opt/' + target_directory)
        ui.separator("line")
    
    interact.enter_to_continue()

def is_installing():
    avail = ["tar.gz", "tar.xz"]
    file_path = str(input('Type /path/to/your/file: '))
    cons_file_path = file_path
    
    if(len(cons_file_path) > 12):
        pass
    else:
        menu()

    extract_arg: str
    all_good = False
    
    for ext in avail:
        if ext in file_path:
            #print(ext)
            extract_arg = ext
            all_good = True
            print("this is working.")
            break
    else:
        print("Type a valid 'tar' file/path.")
    
    if(all_good):
        extract(extract_arg, file_path)
        

    menu()


def choose():
    avail = ["1", "2", "3", "4"]
    cons = input('Type your option: ')

    if(cons=="00"):
        ui.clear()
        exit()

    if(cons=="99"):
        interact._exec("python3 $PACCINO_PATH/main.py")
        exit()

    if(cons in avail):
        if(cons=="1"):
            is_installing()
        elif(cons=="2"):
            dir_name = input('Remove: ')
            if(len(dir_name) > 2):
                cont = input("Continue? (y/N): ")
                if(cont=="y"):
                    ui.separator("line")
                    comm = 'sudo rm -rf /opt/' + dir_name
                    interact._exec(comm)
                    ui.separator("enter")
                    print(dir_name + ' has been removed.')
                    ui.separator("line")
                    interact.enter_to_continue()
                else:
                    pass
            else:
                pass
        elif(cons=="3"):
            comm = 'cd /opt; ls; cd $HOME'
            ui.separator("line")
            interact._exec(comm)
            ui.separator("line")
            interact.enter_to_continue()
        elif(cons=="4"):
            ui.clear()
            ui.separator("line")
            interact._exec("cat $PACCINO_PATH/tar_help.pc")
            ui.separator("line")
            interact.enter_to_continue()

    menu()

def menu():
    ui.clear()
    ui.header("no title")
    print("Paccino 'tar' manager.")
    ui.separator("line")
    print(colored("[1] Extract", "green"))
    print(colored("[2] Remove", "magenta"))
    print(colored("[3] List", "cyan"))
    print(colored("[4] Help", "yellow"))
    ui.separator("enter")
    print(colored("[99] Exit", "cyan"))
    print("[00] Quit")
    ui.separator("line")
    choose()

menu()
