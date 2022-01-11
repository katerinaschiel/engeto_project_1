# Texts

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# Extras
separator = "-" * 35

# Registered users

data = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Get username and PW
username = input("username: ")
password = input("password: ")
print(separator)

# Check if username and PW are correct
if data.get(username) == password:
    print(f"Welcome to the app {username}!")
    print("We have 3 texts to be analyzed.")
    print(separator)
else:
    print("Unregistered user, terminating the program ...")
    print(separator)
    quit()

# Offer texts to be analyzed and check response
choice = input("Enter a number btw. 1 and 3 to select: ")
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and type(choice) != int:
    print("Such text is not in the offer, please try again.")
    quit()

else:
    print(f"You have selected a text # {choice}.")
    print(separator)
    choice = int(choice)

# cleared texts (divided to words)
chosen_text = TEXTS[choice - 1]
cleared_text = []

for word in chosen_text.split():
    word = word.strip(".:;,")
    if word.isalpha() or word.isalnum():
        cleared_text.append(word)

# word count
word_count = len(cleared_text)
print(f"The number of words in this text is: {word_count}.")

# titlecase words
titlecase = 0
for words in cleared_text:
    if words.istitle():
        titlecase = titlecase + 1
        continue

print(f"There are {titlecase} lower case words in this text.")

# uppercase words
uppercase = 0
for words in cleared_text:
    if words.isupper():
        uppercase_1 = uppercase + 1
        continue

print(f"There are {uppercase} upper case words in this text.")

# lowercase words
lowercase = 0
for words in cleared_text:
    if words.islower():
        lowercase = lowercase + 1
        continue

print(f"There are {lowercase} upper case words in this text.")

# numeric count & sum
numeric = 0
sum = 0
for words in cleared_text:
    if words.isnumeric():
        numeric = numeric + 1
        sum = sum + int(words)
        continue

print(f"There are {numeric} numeric strings in this text.")
print(f"The sum of all the numbers is {sum}.")

# NEFUNGUJE

# Length of words
words_len = []
for word in cleared_text:
    words_len.append(len(word))

# Frequency of words' lengths
freq_words_len = {}
for word in words_len:
    if word not in freq_words_len:
        freq_words_len[word] = 1
    else:
        freq_words_len[word] = freq_words_len[word] + 1

# Cosmetics for graph
for lenght, count in sorted(freq_words_len.items()):
    stars = "*" * count
    print(f"{(lenght):>2} | {(stars):<14} | {(count)}")
print(separator)
print("Thank you for using our app =)")