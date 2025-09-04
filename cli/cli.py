from cli.actions import ACTIONS
import sys

options = [i for i in range(len(ACTIONS))]
def start_cli(connection):
    while (True):
        print("\n")
        for i, action in enumerate(ACTIONS):
            print(f"({i}) - {action.get_view()}")
        try:
            option_selected = input("Enter number corresponding to desired action above. Ctr-C to exit: ")
        except KeyboardInterrupt as e:
            print("Exiting...")
            return
        try: 
            option_selected = int(option_selected)
        except Exception as e:
            print(f"\nInvalid input - given: {option_selected} options: {options}")
            print("Please try again")
            continue

        if option_selected < 0 or option_selected >= len(ACTIONS):
            print(f"\nInvalid input - given: {option_selected} options: {options}")
            print("Please try again")
            continue
        
        ACTIONS[option_selected].run(connection)

def get_optional_args():
    db_args = {'user': 'root', 'password': 'password', 'host': 'localhost', 'port': 3306, 'database': 'ticket_system'}
    if (len(sys.argv) < 1):
        return db_args
    for i, arg in enumerate(sys.argv):
        if (i == 0):
            continue
        key, value = arg.split("=")
        if key in db_args:
            db_args[key] = value
    return db_args
            



