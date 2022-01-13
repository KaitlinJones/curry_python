# else keyword with loops
languages = ["C++", "Java", "Python", "Javascript", "Python"]

print("What are you searching for?")
lang = input()

for language in languages:
    if language == lang:
        print(language + " was found.")
        break
else: 
    print("not found")
