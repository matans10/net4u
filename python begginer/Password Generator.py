import random
import string

##it somewhat over only to put it in functions

print("===Password Generator===")
print("   ==================  ")
enter=1
while(enter==1):
    difficulty = int(input("choose strengh of password:\n1.weak\n2.medium\n3.strong\n>> "))
    while(True):
        long = input("how long do you want your passward to be? ")
        if long < 8:
            print("too short , password hasto be above 8 digits")
        elif long >= 8:
            break
        else:
            print("worng input , please enter a integer")

    if difficulty == "1":
        s=''.join(random.choice(string.digits) for i in range(long))
    elif difficulty == "2":
        s=''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(long))

    elif difficulty == "3":
        s = ''.join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase ) for i in range(long))
    else:
        print("worng input")

    print(s)

    while(True):
        ok = input("are you happy with your password ? [y/n]")
        if ok=="n" or ok=="N":
            break
        elif ok=="y" or ok=="Y":
            enter="0"
            break
        else:
            print("wrong input")
