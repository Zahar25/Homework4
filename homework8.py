lst = [2, 4, 6, 8, 10]
def func(lst, shift):
    return lst[-shift:] + lst[:-shift]
print(func(lst,shift=int(input("Enter number: "))))