#input
txt = input()
letter = input()

#count lenght and amount of letter in txt
lenght = len(txt)
amount = txt.count(letter)
res = amount/lenght * 100
print(int(res))