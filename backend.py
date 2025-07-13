import os
import termcolor
from termcolor import colored
import func

prob_null = [None, ""]

f = func

class Options:
    def __init__(self):
        pass

    def install(self):
        all_good: bool
        for_all_good = 0
        f.UI().clear()
        f.UI().header("install")
        f.UI().separator("line")
        while True:
            cons_to_install = input('Package name: ')
            if(len(cons_to_install) > 1 and cons_to_install not in prob_null):
                for_all_good += 1
                pass
            else:
                break;

            cons_try_in = input("Manager (pacman/yay): ")
            if(cons_try_in not in prob_null):
                for_all_good += 2
                pass
            else:
                break;

            if(for_all_good >= 2):
                all_good = True

            if(all_good):
                f.UI().separator("line")

            try_in = cons_try_in
            package = cons_to_install
            if(package and try_in not in prob_null):
                if(try_in == "pacman"):
                    #print("THIS IS WORKING LOL") #DEBUG
                    comm = 'sudo ' + try_in + ' -S ' + package
                    f.Interact()._exec(comm)
                    break;
                elif(try_in=="yay"):
                    comm = try_in + ' -S ' + package
                    f.Interact()._exec(comm)
                    break;
                else:
                    break;
            else:
                break;

    def remove(self):
        f.UI().clear()
        f.UI().header("remove")
        f.UI().separator("line")
        cons = input("Package name: ")
        while True:
            if(len(cons) > 1 and cons not in prob_null):
                com = 'sudo pacman -R $(pacman -Qq | grep "' + cons + '")'
                f.UI().separator("line")
                f.Interact()._exec(com)
                break;
            else:
                break;

    def search(self):
        f.UI().clear()
        f.UI().header("search")
        f.UI().separator("line")
        cons = input("Search: ")
        if(len(cons) > 1 and cons not in prob_null):
            f.UI().separator("line")
            to_exec = 'pacman -Ssq ' + cons + '| column'
            f.Interact()._exec(to_exec)
        else:
            pass

    def upgrade(self):
        f.Interact()._exec("sudo pacman -Syu")

    def autoclean(self):
        f.Interact()._exec("sudo pacman -R $(pacman -Qtdq)")

    def cache_clean(self):
            f.Interact()._exec("sudo pacman -Scc; yay -Scc")

    def list(self):
        f.UI().clear()
        f.Interact()._exec("pacman -Qq | column | less")

    def help(self):
        f.UI().clear()
        f.UI().separator("line")
        f.Interact()._exec("cat $PACCINO_PATH/help.pc")

    def revert(self):
        f.Interact().warning()
        print('Type' + colored(' "list" ', "blue") + 'to show cached pkg files.')
        print('Type' +  colored(' "install" ', "yellow") + 'to continue.')
        menu_command = input('command: ')
        if(menu_command=="list"):
            f.UI().separator("line")
            f.Interact()._exec("cd /var/cache/pacman/pkg && ls *.pkg.tar.zst && cd $HOME")
            f.UI().separator("enter")

        elif(menu_command=="install"):
            f.UI().separator("line")
            print(colored('note: type "cache" to automatically install cached pkg file.', "cyan"))
            cons = input("path/to/file to install: ")
            if(cons=="cache"):
                cons_2 = input('Archive Package Name: ')
                comm = 'sudo pacman -U /var/cache/pacman/pkg/' + cons_2
            else:
                comm = 'sudo pacman -U ' + cons

            if(comm!=None):
                f.UI().separator("line")
                f.Interact()._exec(comm)
            else:
                pass

