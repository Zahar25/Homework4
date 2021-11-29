def is_prime(num):
    a=[]
    for i in range (1, 1000):
        if (num/i).is_integer():
            a.append(i)
    if len(a)==2:
        print("True")
    else:
        print("False")
is_prime(int(input("Enter number:")))