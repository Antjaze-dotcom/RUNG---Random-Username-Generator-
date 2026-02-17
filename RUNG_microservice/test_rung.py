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
