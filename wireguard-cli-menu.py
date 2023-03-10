import subprocess
from simple_term_menu import TerminalMenu

#wireguard commands for furthor use
wg_up = ("sudo","wg-quick","up","wg0")
wg_down = ("sudo","wg-quick","down","wg0")
wg_enable = ("sudo","systemctl","enable","wg-quick@wg0")
wg_disable = ("sudo","systemctl","disable","wg-quick@wg0")

#clear function for menu tidying
def menu_clear():
    subprocess.run("clear")

#loop will only exit when user selects exit
while True:
    
    #main menu prompt
    menu_clear()
    menu_title = ("Main menu for wireguard CLI\n1,Make sure your wireguard config file is in /etc/wireguard\n2,Rename the config file wg0.conf\n")
    options = (["Start Wireguard", "Stop Wireguard", "Enable Wireguard on startup", "Disable Wireguard on startup","Exit"])
    main_menu_cursor_style = ("fg_gray", "bold")
    #main menu options
    terminal_menu = TerminalMenu(
    menu_entries=options,
    title=menu_title,
    menu_cursor="-",
    menu_cursor_style=main_menu_cursor_style
    )
    
    menu_entry_index = terminal_menu.show()
    menu = (options[menu_entry_index])

    #runs wireguard if user selects to start
    if menu == ("Start Wireguard"):
        menu_clear()
        subprocess.run(wg_up)
        input("wireguard is running! Press enter to the main menu\n")
        continue
    
    #stops wireguard if user selects to top
    elif menu == ("Stop Wireguard"):
        menu_clear()
        subprocess.run(wg_down)
        input("wireguard is not running! Press enter to the main menu\n")
        continue
    
    elif menu == ("Enable Wireguard on startup"):
        menu_clear()
        subprocess.run(wg_enable)
        input("wireguard is enabled on startup! Press enter to the main menu\n")
        continue
    
    elif menu == ("Disable Wireguard on startup"):
        menu_clear()
        subprocess.run(wg_disable)
        input("wireguard is disabled on startup! Press enter to the main menu\n")
        continue
        
    #exits program
    elif menu == ("Exit"):
        print("have a good one!")
        break
