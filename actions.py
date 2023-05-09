from constants import LEVEL_SLOTS_MAPPING, LEVELS
from storage import CAR_SLOT_STORAGE, REMAINING_SLOT_STORAGE


def initialize_storage():
    global REMAINING_SLOT_STORAGE
    slot_no = 0
    for level in LEVELS:
        slots = LEVEL_SLOTS_MAPPING.get(level) or 0
        REMAINING_SLOT_STORAGE[level] = [
            slot_no + slot_cnt for slot_cnt in range(1, slots + 1)
        ]
        slot_no += slots
    return True


def get_slot(car_id):
    if not car_id:
        return None, "Please Enter valid car number"
    global CAR_SLOT_STORAGE
    parking_slot = CAR_SLOT_STORAGE.get(car_id, {}) or {}
    msg = ""
    if not parking_slot:
        msg = f"Your car is not parked here, better luck next time!!!"
    else:
        msg = f"Your car with number {car_id} is parked at, \nLevel:{parking_slot.get('level')} \nSlot No.:{parking_slot.get('slot')}"
    return parking_slot.get("slot"), msg


def park_car(car_id):
    global CAR_SLOT_STORAGE, REMAINING_SLOT_STORAGE
    if not car_id:
        return None, "Please Enter valid car number"
    if CAR_SLOT_STORAGE.get(car_id):
        return None, f"Car with number {car_id} is already parked here."
    level_found = next(
        (level for level in LEVELS if REMAINING_SLOT_STORAGE.get(level, [])), None
    )
    slot_found = None
    if not level_found:
        msg = f"Sorry, parking is full. please try aftre sometime."
    else:
        # allcatting parking
        slot_found = REMAINING_SLOT_STORAGE[level_found][0]
        # changing remaining slots
        REMAINING_SLOT_STORAGE[level_found] = REMAINING_SLOT_STORAGE[level_found][1:]
        # setting in storage
        CAR_SLOT_STORAGE[car_id] = {"level": level_found, "slot": slot_found}
        msg = f"Your car with number {car_id} is parked at, \nLevel:{level_found} \nSlot No.:{slot_found}"
    return slot_found, msg


def remove_car(car_id):
    global CAR_SLOT_STORAGE, REMAINING_SLOT_STORAGE
    parking_slot = CAR_SLOT_STORAGE.get(car_id, {}) or {}
    msg = ""
    if not parking_slot:
        msg = f"Your car is not parked here, better luck next time!!!"
    else:
        msg = f"Your car with number {car_id} was parked at, \nLevel:{parking_slot['level']} \nSlot No.:{parking_slot['slot']}"
        # removing car from storage
        del CAR_SLOT_STORAGE[car_id]
        # changing remaining slots
        REMAINING_SLOT_STORAGE[parking_slot["level"]].append(parking_slot["slot"])
    return parking_slot.get("slot"), msg


def get_car_number(count=3):
    msg = ""
    car_id = None
    while count > 0:
        car_id = input("Enter car number to proceed: ")
        if not car_id:
            count -= 1
            print(f"{count} attempts left please enter valid Car number.")
            continue
        else:
            break
    if not car_id:
        msg = "Action can not be performed as no valid car number entered."
    return car_id or False, msg


def perform(option):
    msg = ""
    slot, car_id, msg = None, None, None
    # evaluating options
    if option == "1":
        # parking car
        car_id, msg = get_car_number()
        slot, msg = park_car(car_id)
    elif option == "2":
        # removing car
        car_id, msg = get_car_number()
        slot, msg = remove_car(car_id)
    elif option == "3":
        # get parked slot
        car_id, msg = get_car_number()
        slot, msg = get_slot(car_id)
    else:
        msg = "Select valid option please..."
    return slot, car_id, msg
