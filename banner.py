import pyfiglet
from termcolor import colored


def show_banner(tool_name):
    ascii_banner = pyfiglet.figlet_format(tool_name)
    print(colored(ascii_banner, 'red', attrs=['bold']))
    print(' '*20, colored('@manikanta1404', 'green'))

show_banner("Password Generator")
