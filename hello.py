# lists

import copy

my_favorite_things = ["working out", 7, ['amazon prime', ['netflix', 'hulu']]]
c = copy.deepcopy = my_favorite_things.copy()

print(c)

print(id(c[2]))
print(id(my_favorite_things[2]))

print(my_favorite_things, c)