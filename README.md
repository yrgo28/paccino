# Paccino
pacman/yay minimal termial interface

Paccino is a script written in python. Works like a minimal terminal tool to manage pacman/yay basic functions. Made by a begginner, for begginners.

Use: All options are enumerated. Type option number and press enter to execute it.

# DEPENDENCES:

1. python3 (sudo pacman -S python3)
2. python-termcolor (install with: pip install termcolor)
3. yay (for AUR packages)

# Installation:
- FROM GIT

1. Clone this repository - $: git clone https://github.com/yrgo28/paccino

2. Edit your shell rc file - (if you use bash) sudo text-editor ~/.bashrc (In zshell cases, change ".bashrc" to ".zshrc") eg $: sudo nano .bashrc

3. Type in rc file: export PACCINO_PATH=directory-was-you-cloned-this eg $: export PACCINO_PATH=$HOME/paccino

4. Make an alias for paccino - RCFILE $: alias paccino='python3 $PACCINO_PATH/main.py'

5. Save changes and restart your terminal

6. Type: SHELL: paccino

- FROM RELEASE FILES (zip file):

1. Download it and extract in a directory (unzip paccino.zip paccino/)

2. Edit your shell rc file and add other configs, like installation from git:

$: sudo nano(text editor) .bashrc(shrc file)
shrc: export PACCINO_PATH=directory-you-have-extacted-paccino.zip
shrc: alias paccino='$PACCINO_PATH/main.py'

3. Save changes and restart your terminal

4. Type: paccino, to open it

Thanks for use Paccino Script <3
