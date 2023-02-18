x = int(input())
for i in range(2, x):
    if x % i == 0:
        print(x, "– Its not prime number")
        break
    else:
        print(x, "– Its prime number")
        break