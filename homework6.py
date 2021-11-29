def func (num):
    if num > 0:
        print(num ** 2)
    elif num < 0:
        print(num + 100)
    else:
        print (num)
result = func (int(input("Enter number: ")))