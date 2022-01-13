# flags
numbers = [5, 3, 6, 70, 4, 2, 4, 3]

i = 0
square = 500
success = False #flag

while i < len(numbers):
    if numbers[i] ** 2 > square:
        print (numbers[i], "squared is larger than", square)
        success = True #flag
        break
    print(numbers[i], "squared is not larger than", square)
    i += 1

if not success: #flag test
    print("None of them was large enough")