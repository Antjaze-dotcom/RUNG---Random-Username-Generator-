# RUNG---Random-Username-Generator-
A microservice that can generate up to three unique strings as a usable Username. Also allows for uploading a pool of custom strings through which to generate a username.    

## How to REQUEST data

The program requests data by sending a call to the rung_service.txt file. There can be two different calls. One that requests a username from a defualt list, and another that requests a username to be made from a list, or multiple lists, provided in the call. An example of each call type is provided below:

A REQUEST that includes a custom list

with open("rung_service.txt", "w") as f:
    f.write("Choose_From_1_list\n")
    f.write(",".join(custom_list) + "\n")

A REQUEST for a username that uses a default list



## How to RECIEVE data
