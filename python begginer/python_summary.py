import random
import paramiko
def convert(currency1,currency2,amount):
    dollar = 1; euro = 0.91; shekel = 3.43
    if currency1 == "1":
        currency1 = dollar
    elif currency1 == "2":
        currency1 = euro
    else:
        currency1 = shekel
    if currency2 == "1":
        currency2 = dollar
    elif currency2 == "2":
        currency2 = euro
    else:
        currency2 = shekel
    print("%.2f" % (amount/(currency1/currency2)))

while(True):
    while(True):
        print("menu:\n1.convert Dollar/Euro/Shekel\n2.find your friend's id"
              "\n3.2 times in a row (game)\n4.paramiko")
        menu_input = input("choose 1-4 option:")
        if menu_input != "1" and menu_input != "2" and menu_input != "3" and menu_input != "4":
            print("please choose 1-4 option\n")
        else:
            break
    ##option 1
    if menu_input == "1":
        while(True):
            currency = input("choose first:\n1.dollar\n2.euro\n3.shekel\n")
            if currency != "1" and currency != "2" and currency != "3":
                print("please choose 1-3 option\n")
            else:
                amount = int(input("enter the amount:\n"))
                break
        while(True):
            currency2 = input("choose second:\n1.dollar\n2.euro\n3.shekel\n")
            if currency2 != "1" and currency2 != "2" and currency2 != "3":
                print("please choose 1-3 option")
            else:
                break

        convert(currency,currency2,amount)
    ## option 2
    elif menu_input == "2":
        dicts = {}
        flag = 0
        file = open("file.txt", "w") #reset the txt file
        file.close()
        file = open("file.txt", "a")
        for i in range(2):
            name = input("enter your friend name:")
            dicts[name] = input("enter your friend id:")
            file.write(name + " " + dicts[name] + "\n")
        file.close()
        friend_id = (input("enter the id of the friend you want so search:"))

        file = open("file.txt", "r")
        for line in file:
            single_line = line.split()
            if friend_id == single_line[1]:
                print("your friend is in the list")
                flag = 1
                break
        if flag == 0:
            print("your friend isn't on the list")
    ## option 3
    elif menu_input == "3":
        x1=0 ; sum=0 ;  x=0
        for i in range(10):
            x1 = x
            x=random.randrange(1,6)#here i likened the range to a dice throw
            print(x)
            if x1 == x:
               sum += 10
        print("you earnd :" + str(sum) + " dollars")
    ## option 4
    elif menu_input == "4":
        ip = input("enter the ip of the remote machine:")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username='matan', password='rootroot') #here you should change the username and the passward to your own
        client.exec_command("touch /home/matan/Desktop/done_paramiko.txt") #here you hould change the path as you wish
        client.close()

    exit = input("do you want to exit the program? press any key other then \"Y/y\" to exit")
    if exit != "y" or exit != "Y":
        break
