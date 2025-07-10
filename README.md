# Paccino
pacman/yay terminal minimal interface

Paccino is a script written in python. Works like a minimal terminal tool to manage pacman/yay basic functions. Made by a begginner, for begginners.

Use: Type your option with they number and nothing else :)

DEPENDENCES:

1. python3
2. python-termcolor (install with: pip install termcolor)
3. yay (for AUR packages)

Installation:

//Copy after the "$: "

1. Clone this repository - $: git clone https://github.com/yrgo28/paccino

2. Edit your shell rc file - (if you use bash) sudo text-editor ~/.bashrc (In zshell cases, change ".bashrc" to ".zshrc") eg $: sudo nano .bashrc

3. Type in rc file: export PACCINO_PATH=directory-was-you-cloned-this eg $: export PACCINO_PATH=$HOME/paccino

4. Make an alias for paccino - RCFILE $: alias paccino='python3 $PACCINO_PATH/main.py'

5. Save changes and restart your terminal

6. Type: SHELL: paccino

7. Enjoy!
