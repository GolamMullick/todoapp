for Fizzbuzz in range(1, 101):
    if Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        continue
    elif Fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif Fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(Fizzbuzz)
