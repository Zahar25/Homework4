def prime_list(num_1, num_2):
    for num in range(num_1, num_2 +1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime_list(int(input("Enter first number:")), int(input("Enter second number: ")))
