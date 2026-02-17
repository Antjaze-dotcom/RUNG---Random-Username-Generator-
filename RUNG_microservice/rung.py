# Random Username Generator

import time
import random

# name lists can be customized to fit the main program
# example: adjective + verb + noun = "Mighty Defending Legend"
list1 = ["Bright", "Rapid", "Epic", "Sharp", "Mighty", "Turbo", "Hyper", "Supreme", "Dynamic", "Fearless"]
list2 = ["Running", "Calculating", "Defending", "Enchanting", "Avenging", "Storming", "Reigning", "Rising", "Roaring", "Flying"]
list3 = ["Captain", "Wizard", "Legend", "Knight", "Champion", "Leader", "General", "Scout", "Hero", "Ace"]


while True:
    time.sleep(1)
    with open("rung-service.txt", "r") as f:
        text = f.read()

    username = None

    if text == "generate3":
        username = f"{random.choice(list1)} {random.choice(list2)} {random.choice(list3)}"
 
    elif text == "generate2":
        username = f"{random.choice(list1)} {random.choice(list3)}"

    elif text == "generate1":
        username = f"{random.choice(list3)}"

#   elif text == a list???

    if username:
        with open("rung-service.txt", "w") as f:
            f.write(username)
