def search(text, word):
    txt = text.count(word)
    if txt == 0:
        return("Word not found")
    else:
        return("Word found")
        
text = input()
word = input()

print(search(text, word))