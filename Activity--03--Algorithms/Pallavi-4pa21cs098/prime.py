num = int(input("Enter a number: "))
flag = True
if num > 1:
    for i in range(2,num//2 + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        print("Prime number")
    else:
        print("Not a Prime number")
else:
    print("Not a Prime number")