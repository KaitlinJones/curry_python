# break statement
languages = ["C++", "Java", "Python", "Javascript"]

print("What are you searching for?")
lang = input()

for language in languages:
    print(language)
    if language == lang:
        print("We found " + lang)
        break
    print("End of iteration")





