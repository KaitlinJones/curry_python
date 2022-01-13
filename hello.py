# else clause combined with while loop
numbers = [5, 3, 6, 7, 4, 2, 4, 3]

i = 0
square = 500

while i < len(numbers):
    if numbers[i] ** 2 > square:
        print (numbers[i], "squared is larger than", square)
        break
    else:
        print(numbers[i], "squared is not larger than", square)
    i += 1

else: 
    print("None squared are larger than", square)