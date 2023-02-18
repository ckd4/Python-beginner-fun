def letter_count(text, letter):
    txt = text.count(letter)
    return txt

text = input()
letter = input()

print(letter_count(text, letter))