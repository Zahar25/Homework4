def foo(lst: list):
    temp = list(map(lambda x: x, lst))
    for item in set(temp):
        print(f'{item}: {temp.count(item)}')
foo(['Geek', 'Hub', 'Hub', 'Geek', 'Hub', 5, 10, 15, 15, 15, 10, 5, 10, 'Geek', 'Hub', 5])