# test file for Random Username Generator microservice

import time

# generate username with three names
with open("rung-service.txt", "w") as f:
    f.write("generate3")
time.sleep(5)
with open("rung-service.txt", "r") as f:
    rand_username = f.read()
    print(f"{rand_username}")

# generate username with two names
with open("rung-service.txt", "w") as f:
    f.write("generate2")
time.sleep(5)
with open("rung-service.txt", "r") as f:
    rand_username = f.read()
    print(f"{rand_username}")

# generate username with one name
with open("rung-service.txt", "w") as f:
    f.write("generate1")
time.sleep(5)
with open("rung-service.txt", "r") as f:
    rand_username = f.read()
    print(f"{rand_username}")

# generate username from a list

# lists that can be edited
editable_list1 = ["General","Commander","Captain","Marshal","Horde Master","King","Queen","Prince","Princess","Lord","Lady"]
editable_list2 = ["Isovel","Ralif","Astrol","Trech","Pragmantia","Yorsif","Hreect","Malidour"]
editable_list3 = ["The Great","The Terrible","The Loathsome","The Stinky","The Horror","The Magnificent"]

#Genereate username from three imported lists
with open("rung_service.txt", "w") as f:
    f.write("Choose_From_3_list\n")
    f.write(",".join(editable_list1) + "\n")
    f.write(",".join(editable_list2) + "\n")
    f.write(",".join(editable_list3) + "\n")
time.sleep(5)
with open("rung_service.txt", "r") as f:
    rand_username = f.read().strip()
    print(f"{rand_username}")

#Generate username from two imported lists
with open("rung_service.txt", "w") as f:
    f.write("Choose_From_2_list\n")
    f.write(",".join(editable_list1) + "\n")
    f.write(",".join(editable_list2) + "\n")
time.sleep(5)
with open("rung_service.txt", "r") as f:
    rand_username = f.read().strip()
    print(f"{rand_username}")

# generate username from one imported list
with open("rung_service.txt", "w") as f:
    f.write("Choose_From_1_list\n")
    f.write(",".join(editable_list1) + "\n")
time.sleep(5)
with open("rung_service.txt", "r") as f:
    rand_username = f.read().strip()
    print(f"{rand_username}")
