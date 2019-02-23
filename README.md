# Python Interactive Dictionary

Implements the following features:

1. Loads the dictionary dataset into the "data" variable using the *json.load* method. Accepts a word from the user and returns the definition from the database if it exists.

```python
import json

def find(w):
    if w in data:
        return data[w]
    else:
        return "Word not found in the dictionary"

data = import.json("data.json")
word = input("Enter a word: ")
print(find(word))
```

2. Account for case sensitivity. Convert the word entered by the user to lowercase using the *.lower()* method.

```python
import json

def find(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Word not found in the dictionary"

data = import.json("data.json")
word = input("Enter a word: ")
print(find(word))
```

3. Account for word misspellings using the difflib library. You can get a complete list of Python standard libraries from https://docs.python.org/3/library/. The difflib library library implements a *get_close_match* class that accepts the word and possibilities as arguments and returns a similar word if the similarity is greater than a certain offset value.

```python
import json
from difflib import get_close_match

def find(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean '%s' instead? Enter 'Y' if yes or 'N' if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word is not in the dictionary. Please try again."
        else:
            return "Please check your query."
    else:
        return "Word not found in the dictionary"

data = import.json("data.json")
word = input("Enter a word: ")
print(find(word))
```
4. Iterate though the final definitions list. iterate through this list and output the definitions.

```python
word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
```

