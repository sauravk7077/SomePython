from colorama import init,Fore

init()


"""
This method displays the message in different colors depending on the info_level
Parameters:
    message (str): The message to be displayed
    info_level: The values are 'info', 'warning', 'error'. These values determine the color of message.
"""
def show_info(message, info_level='info'):
    if info_level.lower() == "error":
        print(Fore.RED + "Error!")
    elif info_level.lower() == "warning":
        print(Fore.YELLOW + "Warning!")
    else:
        print(Fore.CYAN + "Info!")
    print(message)
