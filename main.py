# parking lot main file to start work
import actions


def start_praking():
    # taking input to start parking
    while True:
        start = input("Enter yes if you want to start parking cars(YES/NO): ")
        if start and start.lower() == "yes":
            break
        elif start and start.lower() == "no":
            return None
        print("Enter valid input to start")
    print("Type :q to exit from parking or Ctrl+C or Ctrl+Z\n\n")
    # initializing storage
    actions.initialize_storage()
    # starting parking
    while True:
        option = input(
            """
            Select options from below to perform any action
            1. Park Car
            2. Remove Car
            3. Get slot number of car
            :q to quit parking program
            
            Enter selection (ex.: 2): """
        )
        if option and option.lower() == ":q":
            print("Exiting Parking program...")
            return
        _, _, msg = actions.perform(option)
        print()
        print("-" * len(msg))
        print(msg)
        print("-" * len(msg))


start_praking()
