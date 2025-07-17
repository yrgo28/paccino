import os
import termcolor
from termcolor import colored
import welcome

def terminal_size():
    num = os.get_terminal_size().columns
    return num

class UI:
    def __init__(self):
        pass

    def header(self, arg: str):
        avail = ["main", "more", "start", "install", "remove", "search", "secure-mode", "no title"]
        num = terminal_size()
        if(num < 72):
            print("Terminal columns is minor than 72, graphics bugs are so possibly")

        welcome.ascii().print_ascii()
        if(arg in avail):
            if(arg=="main"):
                print("Main menu.")
                pass
            elif(arg=="more"):
                print("Other options.")
                pass
            elif(arg=="start"):
                print("Start menu.")
                pass
            elif(arg=="install"):
                print("Install new package.")
                pass
            elif(arg=="remove"):
                print("Remove packages.")
                pass
            elif(arg=="search"):
                print("Search a package.")
                pass
            elif(arg=="secure-mode"):
                print("Secure mode menu.")
            elif(arg=="no title"):
                pass
        else:
            print("Error: Header not found.")

    def clear(self):
        os.system("clear")
    
    def separator(self, separator_type: str):
        types = ["enter", "line"]
        if(separator_type in types):
            pass
        elif(separator_type not in types or separator_type == None):
            separator_type = "enter"

        if(separator_type == "line"):
            print("=" * terminal_size())
        elif(separator_type == "enter"):
            print(" ")

class Interact:
    def __init__(self):
        pass
    
    def enter_to_continue(self):
        cons = input("press [enter] to continue...")

    def _exec(self, arg):
        os.system(arg)

    def warning(self):
        print(colored("Take with your own risk!", "red"))
        print(colored("info: you can cancel this just typing [enter] right now.", "yellow"))


