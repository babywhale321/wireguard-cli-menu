import subprocess

#wireguard commands for furthor use
wg_up = ("sudo","wg-quick","up","wg0")
wg_down = ("sudo","wg-quick","down","wg0")

#clear function for menu tidying
def menu_clear():
    subprocess.run("clear")

#loop will only exit when user inputs "3"
while True:
    
    #main menu prompt
    menu_clear()
    print("if you havent already done so make sure to have wg0.conf in /etc/wireguard before starting wireguard.")
    menu = input("Press 1 to start wireguard\nPress 2 to stop wireguard\nPress 3 to exit program\n")

    #runs wireguard if user inputs 1
    if menu == "1":
        menu_clear()
        subprocess.run(wg_up)
        input("wireguard is running! Press enter to the main menu\n")
        continue
    
    #stops wireguard if use inputs 2
    elif menu == "2":
        menu_clear()
        subprocess.run(wg_down)
        input("wireguard is not running! Press enter to the main menu\n")
        continue
    
    #exits program
    elif menu == "3":
        print("have a good one!")
        break
    
    #anything other then 1,2 or 3 will get an error message
    else:
        menu_clear()
        input("Please select an option with a number associated with the action.\nPress enter for the main menu.\n")
        continue
