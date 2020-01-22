#this projext was done on linux (ubuntu)

#!bin/python3

import os

os.system("touch /home/{user_name}/Desktop/py/py_script | echo \"someone\nsomewhere\nsomehow\" >> /home/{user_name}/Desktop/py/py_script")

file = open"(/home/{user_name}/Desktop/py/py_script" , "r+")

for line in file:
  print(line)
file.close()

file = open("/home/{user_name}/Desktop/py/py_script" ,"a")
file.write("John Doe and his family")
file.close()

os.system("mv /home/{user_name}/Desktop/py/py_script /home/{user_name}/Desktop/")
