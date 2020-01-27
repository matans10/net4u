def fibonacci_calculation(times):
    for i in range(int(times)):
        if(i==0):
            print("1")
        elif (i==1):
            fibunacci_number = 1
            prev_num = 0
            fibunacci_number = prev_num + fibunacci_number
            print(str(fibunacci_number))
            prev_num = prev_num+fibunacci_number
        else:
            new_fibunacci_number = fibunacci_number + prev_num
            print(new_fibunacci_number)
            prev_num = fibunacci_number
            fibunacci_number = new_fibunacci_number


print("The Fibonacci game")
times = input("Enter hoe many numbers of the Fibonacci seqeunce you want to print:")
fibonacci_calculation(times)
