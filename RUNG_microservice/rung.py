import time
import random

# name lists can be customized to fit the main program
# example: adjective + verb + noun = "Mighty Defending Legend"
list1 = ["Bright", "Rapid", "Epic", "Sharp", "Mighty", "Turbo", "Hyper", "Supreme", "Dynamic", "Fearless"]
list2 = ["Running", "Calculating", "Defending", "Enchanting", "Avenging", "Storming", "Reigning", "Rising", "Roaring",
         "Flying"]
list3 = ["Captain", "Wizard", "Legend", "Knight", "Champion", "Leader", "General", "Scout", "Hero", "Ace"]

while True:
    time.sleep(1)
    with open("rung-service.txt", "r") as f:
        firstline = f.readline().strip()  # readline calls next line in txt each time called, strip() removes \n

        username = None

        # For unsername generation from default lists

        if firstline == "generate3":
            username = f"{random.choice(list1)} {random.choice(list2)} {random.choice(list3)}"

        elif firstline == "generate2":
            username = f"{random.choice(list1)} {random.choice(list3)}"

        elif firstline == "generate1":
            username = f"{random.choice(list3)}"


        # For custom usernames from imported list

        elif firstline == "Choose_From_1_list":
            secondline = f.readline()
            list1 = [name.strip() for name in secondline.split(",")]  # name.strip() removes \n for names at end of lists
            username = f"{random.choice(list1)}"  # chooses random name in list
            with open("rung-service.txt", "w") as p:
                p.write(username)

        elif firstline == "Choose_From_2_list":
            secondline = f.readline()
            thirdline = f.readline()
            list1 = [name.strip() for name in secondline.split(",")]
            list2 = [name.strip() for name in thirdline.split(",")]
            username = f"{random.choice(list1)} {random.choice(list2)}"
            with open("rung-service.txt", "w") as p:
                p.write(username)

        elif firstline == "Choose_From_3_list":
            secondline = f.readline()
            thirdline = f.readline()
            fourthline = f.readline()
            list1 = [name.strip() for name in secondline.split(",")]
            list2 = [name.strip() for name in thirdline.split(",")]
            list3 = [name.strip() for name in fourthline.split(",")]
            username = f"{random.choice(list1)} {random.choice(list2)} {random.choice(list3)}"
            with open("rung-service.txt", "w") as p:
                p.write(username)

        if username:
            with open("rung-service.txt", "w") as f:
                f.write(username)
