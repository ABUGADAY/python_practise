favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'das': 'c++',
}

language = favorite_language['das'].title()
print(f"Das's favorite language is {language}.")

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_language.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_language:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

#去重
print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'das': ['c++', 'java'],
}

for name, languages in favorite_language.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")