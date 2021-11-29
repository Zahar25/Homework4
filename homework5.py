def fibonacci (n):
    f1, f2 = 0, 1
    print(f1, f2, end = ' ')
    while f2 < n:
        print (f2, end=' ')
        f1, f2 = f2, f1 + f2
fibonacci(n = int(input("Enter number: ")))
