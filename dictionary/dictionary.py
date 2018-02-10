import json
from difflib import get_close_matches   

# Reading dictionary file that has all words with meaning.
data = json.load(open("data.json"))

# Function to find a word in dictoinary.
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title()in data:       # Capitalize first letter of word and then search in the dictionary. Helps in finding name of cities or countries etc.
        return data[word.title()]
    elif word.upper() in data:      # Capitalize whole word of accronyms.
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        reply = input("Did you mean %s? (Yes / No): " % get_close_matches(word, data.keys())[0])
        while reply != "Yes" and reply != "No":     # Loop till user enters a valid input.
            reply = input("Please enter Yes or No : ")
        if reply == "Yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif reply == "No":
            return "No match found."
    else:
        return "Word does't exist. Please check the word."


word = input("Enter word: ")        # Take input from user.

output = translate(word)


if type(output) == list:
    i = 1
    for definition in output:
        print(str(i) + ". " + definition)
        i += 1
else:
    print(output)


# How get_close_matches work?
# Takes 4 arguments.
# (if last 2 are not specified, default values are assigned)
# get_close_matches(word, list, n = 3, cutoff = 0.5)
# word:     word to look
# list:     list from where to look
# n:        number of matches to display
# cutoff:   threshold of match ratio, 0.5 is more than 50% matches are displayed.
# get_close_matches("rain", data.keys(), n = 3, cutoff = 0.6)
