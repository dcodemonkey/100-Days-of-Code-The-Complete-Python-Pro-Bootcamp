# Range
# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

for number in range(1,16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5:
        print("Buzz")
    else:
        print(number)