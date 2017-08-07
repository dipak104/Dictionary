import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        res = input("Did you mean %s instead? Enter Y for yes and N for No : " % get_close_matches(w, data.keys())[0])
        if res == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif res == "N":
            return "The word doesn't exists. Please check it again!!"
        else:
            return "We didn't understand the word entered!!"
    else:
        return "The word doesn't exists. Please check it again!!!"

word = input("Enter the word : ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
