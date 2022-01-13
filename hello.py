# continue statement
languages = ["C++", "Java", "Python", "Javascript", "Python"]

print("What are you searching for?")
lang = input()

for language in languages:
    if language == lang:
        print("We found " + lang)
    else:
        print(language + "...Not what we are looking for...")

# searches through the list and continues to search after condition is true...



