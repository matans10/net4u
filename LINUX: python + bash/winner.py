#writting on ubuntu

#!bin/python3

import os

setlist = set()

for i in range(6):
    new_name = input("enter a new name:")
    setlist.add(new_name)

pop_user = setlist.pop()

os.system("cd /home/{user name}/Desktop/py | touch winner.txt")

file = open("/home/{user name}/Desktop/py/winner","w")
file.write(pop_user)
file.close()

os.system("cat /home/{user name}/Desktop/py/winner")
