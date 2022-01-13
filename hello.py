# print range & list:

foods = ["asparagus", "tacos", "strawberries", "yogurt", "bagels"]

for i in range(10):
    print(i, end = " ")
print()

for food in foods:
    print(food, end = " ")
print()

print(len(foods))

for i in range(len(foods)):
    print(i + 1, foods[i], end = " ")
print()





