import math
age = 15
age_str = str(age)
id_age_str = id(age_str)
other = math.floor(2.6)
added = id_age_str + other
added_str = str(added)
length = len(added_str)

print(length)
print(added_str)
print(added)
print(other)
print(id_age_str)


print(len(str(id(str(age))+ math.floor(2.6))))

