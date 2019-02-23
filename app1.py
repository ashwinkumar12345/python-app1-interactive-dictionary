import json
from difflib import get_close_matches
    #To account misspellings
    #Using a library called difflib
    #Get a complete list of Python standard libraries from https://docs.python.org/3/library/

data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #Implement case insensitivity
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: #To account for a word not in the dictionary dataset and not matched as a similar word
        yn = input("Did you mean '%s' instead? Enter 'Y' if yes or 'N' if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word is not in the dictionary. Please try again."
        else:
            return "Please check your query."

    else:
        return "This word is not in the dictionary. Please try again."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
