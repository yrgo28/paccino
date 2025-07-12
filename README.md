# Paccino
pacman/yay minimal termial interface

Paccino is a script written in python. Works like a minimal terminal tool to manage pacman/yay basic functions. Made by a begginner, for begginners.

Use: All options are enumerated. Type option number and press enter to execute it.

# Dependences:

1. python3 (sudo pacman -S python3)
2. python-termcolor (install with: pip install termcolor; or: sudo pacman -S python-termcolor)
3. yay (for AUR packages)

# Installation:

- Getting files:
  
1. Git: git clone https://github.com/yrgo28/paccino
 
2. From Release files. Download and extract it in a directory.
   
- Terminal indentation:

1. Edit your shell rc file: sudo (text-editor) (shell-rc-file)
* e.g: sudo nano .bashrc

2. Type following lines (in this order):
  * export PACCINO_PATH=directory-where-is-paccino-files
  - e.g: export PACCINO_PATH=$HOME/paccino
         
  * alias paccino='$PACCINO_PATH/main.py'

3. Save changes and restart your terminal.

4. Type "paccino" in your terminal to open it

Thanks for use Paccino Script <3
