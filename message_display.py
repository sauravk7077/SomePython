from colorama import init,Fore

init()


'''This method displays the message in different colors depending on the info_level'''
def show_info(message, info_level='info'):
    if info_level.lower() == "error":
        print(Fore.RED + "Error!")
    elif info_level.lower() == "warning":
        print(Fore.YELLOW + "Warning!")
    else:
        print(Fore.CYAN + "Info!")
    print(message)