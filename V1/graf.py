from colorama import *
from serpinski_triangle import triangle
from menger_sponge import gubka
import time
from progress.bar import IncrementalBar

init(autoreset=True)
print(
    Style.BRIGHT + Fore.GREEN + "  ******** ",
    Style.BRIGHT + Fore.RED + "**      ",
    Style.BRIGHT + Fore.CYAN + "   *******  ",
    Style.BRIGHT + Fore.BLUE + "****     **",
)
print(
    Style.BRIGHT + Fore.GREEN + " **////// ",
    Style.BRIGHT + Fore.RED + "/**      ",
    Style.BRIGHT + Fore.CYAN + "  **/////** ",
    Style.BRIGHT + Fore.BLUE + "/**/**   /**",
)
print(
    Style.BRIGHT + Fore.GREEN + "/**       ",
    Style.BRIGHT + Fore.RED + "/**      ",
    Style.BRIGHT + Fore.CYAN + " **     //**",
    Style.BRIGHT + Fore.BLUE + "/**//**  /**",
)
print(
    Style.BRIGHT + Fore.GREEN + "/*********",
    Style.BRIGHT + Fore.RED + "/**      ",
    Style.BRIGHT + Fore.CYAN + "/**      /**",
    Style.BRIGHT + Fore.BLUE + "/** //** /**",
)
print(
    Style.BRIGHT + Fore.GREEN + "////////**",
    Style.BRIGHT + Fore.RED + "/**      ",
    Style.BRIGHT + Fore.CYAN + "/**      /**",
    Style.BRIGHT + Fore.BLUE + "/**  //**/**",
)
print(
    Style.BRIGHT + Fore.GREEN + "       /**",
    Style.BRIGHT + Fore.RED + "/**      ",
    Style.BRIGHT + Fore.CYAN + "//**     ** ",
    Style.BRIGHT + Fore.BLUE + "/**   //****",
)
print(
    Style.BRIGHT + Fore.GREEN + " ******** ",
    Style.BRIGHT + Fore.RED + "/********",
    Style.BRIGHT + Fore.CYAN + " //*******  ",
    Style.BRIGHT + Fore.BLUE + "/**    //***",
)
print(
    Style.BRIGHT + Fore.GREEN + "////////  ",
    Style.BRIGHT + Fore.RED + "//////// ",
    Style.BRIGHT + Fore.CYAN + "  ///////   ",
    Style.BRIGHT + Fore.BLUE + "//      ///",
)
print(Style.BRIGHT + Fore.WHITE + "#" * 47)
print(Style.BRIGHT + Fore.WHITE + "#", Style.BRIGHT + Fore.GREEN + "             Choose one option            ", Style.BRIGHT + Fore.WHITE + "#")
print(Style.BRIGHT + Fore.WHITE + "#" * 47)

print(Style.BRIGHT + Fore.GREEN + "1. Menger sponge")
print(Style.BRIGHT + Fore.GREEN + "2. Serpinski triangle")
print(Style.BRIGHT + Fore.WHITE + "#" * 47)
x = input(Style.BRIGHT + Fore.GREEN + "Write a number:")

if x == "1":
    gubka()
elif x == "2":
    triangle()